import numpy as np
import pandas as pd
import stress_comps_vectorized as scv
import time

t0 = time.time()

outfile = '../results/zhang_lms_fail_posteriors.csv'
t_poster_file = '../results/tect_rake_posteriors_4e5_runs.csv'

lms = pd.read_csv('../../slip_models/zhang/lms_stress_slip.csv', index_col=0)
t_prior_df = pd.read_csv(t_poster_file)
t_priors = t_prior_df.values
del t_prior_df

# some initial constants
n_trials = t_priors.shape[0]
n_points = len(lms.index)
rho = 2700
g = 9.81

# priors for friction (mu) and pore fluid pressure (lamb[da])
mu_lamb_priors = np.random.random([n_trials, 2])

# make dataframe
search_df_cols = ['iter', 'txx', 'tyy', 'txy', 'mu', 'lamb', 'pt_index', 
                  'depth', 'strike', 'dip', 'slip_m', 'slip_rake']

iter_range = np.arange(n_trials, dtype='float')
pt_range = np.arange(n_points, dtype='float')

# make list/array of sets of prior values for each fault point
index_list = [[iter_range[i], mu_lamb_priors[i,0], mu_lamb_priors[i,1],
               t_priors[i,0], t_priors[i,1], t_priors[i,2], pi]
              for i in iter_range for pi in pt_range]

index_array = np.array(index_list)
del index_list

iter_index = np.int_(index_array[:,0].copy() )
pt_index = np.int_(index_array[:,6].copy() )
mu_lamb_prior_array = index_array[:,1:3]
t_prior_array = index_array[:,3:6]
del index_array

search_df = pd.DataFrame(index=np.arange(len(iter_index)),
                         columns=search_df_cols, dtype=float)

search_df['iter'] = iter_index
search_df[['mu', 'lamb']] = mu_lamb_prior_array
search_df['pt_index'] = pt_index
search_df[['txx', 'tyy', 'txy']] = t_prior_array

search_df['mxx'] = 0.
search_df['mxy'] = 0.
search_df['mxz'] = 0.
search_df['myy'] = 0.
search_df['myz'] = 0.
search_df['mzz'] = 0.

lms_fill_cols = ['depth', 'strike', 'dip', 'slip_m', 'slip_rake',
                       'mxx', 'myy', 'mxy', 'mzz', 'mxz', 'myz']

lms_copy_cols = ['depth_km', 'strike_deg', 'dip_deg', 'slp_am_m', 'rake_deg',
                 'xx_stress', 'yy_stress', 'xy_stress', 'zz_stress',
                 'xz_stress', 'yz_stress']

lms_col_array = lms[lms_copy_cols].values
lms_reps = np.tile(lms_col_array, [n_trials, 1])

search_df[lms_fill_cols] = lms_reps
search_df.depth *= 1000
search_df[['mxx', 'myy', 'mxy', 'mzz', 'mxz', 'myz']] *= 1e6


# do the stress calculations
search_df['tau_s'] = scv.strike_shear( strike=search_df.strike,
                                      dip=search_df.dip, rho=rho, g=g,
                                      mxx=search_df.mxx, myy=search_df.myy,
                                      mxy=search_df.mxy, mzz=search_df.mzz,
                                      mxz=search_df.mxz, myz=search_df.myz,
                                      txx=search_df.txx, tyy=search_df.tyy,
                                      txy=search_df.txy, depth=search_df.depth)

search_df['tau_d'] = scv.dip_shear( strike=search_df.strike,
                                      dip=search_df.dip, rho=rho, g=g,
                                      mxx=search_df.mxx, myy=search_df.myy,
                                      mxy=search_df.mxy, mzz=search_df.mzz,
                                      mxz=search_df.mxz, myz=search_df.myz,
                                      txx=search_df.txx, tyy=search_df.tyy,
                                      txy=search_df.txy, depth=search_df.depth)

search_df['sig_n_eff'] = scv.eff_normal_stress( strike=search_df.strike,
                                      dip=search_df.dip, rho=rho, g=g,
                                      mxx=search_df.mxx, myy=search_df.myy,
                                      mxy=search_df.mxy, mzz=search_df.mzz,
                                      mxz=search_df.mxz, myz=search_df.myz,
                                      txx=search_df.txx, tyy=search_df.tyy,
                                      txy=search_df.txy, depth=search_df.depth,
                                      lamb=search_df.lamb)

search_df['tau_mag'] = np.sqrt(search_df.tau_s**2 + search_df.tau_d**2)

# calculate weighted misfits, start filtering
mean_slip = lms.slp_am_m.mean()

search_df['weighted_fail_misfit'] = (np.abs( search_df.tau_mag
                                          - search_df.mu * search_df.sig_n_eff)
                                     * (search_df.slip_m / mean_slip) )

iters = search_df.groupby('iter')
def l2_norm(array):
    return np.linalg.norm(array, 2)

fail_misfit = iters.weighted_fail_misfit.apply(l2_norm)
fail_likelihood = 1 / (fail_misfit / fail_misfit.min() )

rand_filter = np.random.random(n_trials)
keeps = fail_likelihood[fail_likelihood**3 >= rand_filter] # rejection sample

iters_txx = iters.txx.mean()
iters_tyy = iters.tyy.mean()
iters_txy = iters.txy.mean()
iters_mu = iters.mu.mean()
iters_lamb = iters.lamb.mean()

txx_keep = iters_txx[keeps.index]
tyy_keep = iters_tyy[keeps.index]
txy_keep = iters_txy[keeps.index]
mu_keep = iters_mu[keeps.index]
lamb_keep = iters_lamb[keeps.index]

fail_posteriors = pd.concat([txx_keep, tyy_keep, txy_keep, mu_keep, lamb_keep],
                            names = ['txx','tyy','txy','mu','lamb'])

fail_posteriors.to_csv(outfile, index=False)

t1 = time.time()
t_done = (t1 - t0) // 60
print(len(txx_keep))
print(t_done)
