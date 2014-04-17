import numpy as np
import pandas as pd
import stress_comps_vectorized as scv
import halfspace.projections as hsp
import time

t0 = time.time()

outfile = '../results/qi_rough_fail_posteriors.csv'
t_poster_file = '../results/qi_rough_tect_posteriors.csv'

qb = pd.read_csv('../../slip_models/qi/qi_bei_rough_stress.csv', index_col=0)
qp = pd.read_csv('../../slip_models/qi/qi_peng_rough_stress.csv', index_col=0)

lms = pd.concat((qb, qp), axis=0)

np.random.seed(70)

t_prior_df = pd.read_csv(t_poster_file, index_col=0)
t_priors = t_prior_df[['txx', 'tyy', 'txy']].values
#del t_prior_df

# some initial constants
n_trials = t_priors.shape[0]
n_points = len(lms.index)
rho = 2700
g = 9.81

# priors for pore fluid pressure (phi[da])
phi_priors = np.random.random(1e5)
phi_priors = phi_priors[t_prior_df.index]

# make dataframe
search_df_cols = ['iter', 'txx', 'tyy', 'txy', 'mu', 'phi', 'pt_index', 
                  'depth', 'strike', 'dip', 'slip_m', 'slip_rake']

#iter_range = np.arange(n_trials, dtype='float')
iter_range = np.float_(t_prior_df.index.values) 
pt_range = np.arange(n_points, dtype='float')

print('making list of priors')
index_list = [[iter_ind, phi_priors[i], t_priors[i,0], 
               t_priors[i,1], t_priors[i,2], pi]
              for i, iter_ind in enumerate(iter_range) for pi in pt_range]

print('done making list.  Moving on...')
index_array = np.array(index_list)
del index_list

iter_index = np.int_(index_array[:,0].copy() )
pt_index = np.int_(index_array[:,5].copy() )
phi_prior_array = index_array[:,1]
t_prior_array = index_array[:,2:5]
del index_array

print('filling in dataframe')
search_df = pd.DataFrame(index=np.arange(len(iter_index)),
                         columns=search_df_cols, dtype=float)

search_df['iter'] = iter_index
search_df['phi'] = phi_prior_array
search_df['pt_index'] = pt_index
search_df[['txx', 'tyy', 'txy']] = t_prior_array

search_df['mxx'] = 0.
search_df['mxy'] = 0.
search_df['mxz'] = 0.
search_df['myy'] = 0.
search_df['myz'] = 0.
search_df['mzz'] = 0.

lms_fill_cols = ['depth', 'strike', 'dip', 'slip_m',
                 'mxx', 'myy', 'mxy', 'mzz', 'mxz', 'myz']

lms_copy_cols = ['z_center', 'strike','dip','slip_m',
                'xx_stress', 'yy_stress', 'xy_stress', 'zz_stress',
                'xz_stress', 'yz_stress']

lms_col_array = lms[lms_copy_cols].values
lms_reps = np.tile(lms_col_array, [n_trials, 1])

search_df[lms_fill_cols] = lms_reps
search_df.depth *= 1000
search_df[['mxx', 'myy', 'mxy', 'mzz', 'mxz', 'myz']] *= 1e6


# do the stress calculations
print('calculating fault stresses')
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
                                      phi=search_df.phi)

search_df['tau_mag'] = np.sqrt(search_df.tau_s**2 + search_df.tau_d**2)

# calculate weighted misfits, start filtering
mean_slip = lms.slip_m.mean()

search_df['weighted_tau_misfit']=search_df.tau_mag *search_df.slip_m /mean_slip

print('doing groupby')
iters = search_df.groupby('iter')

print('filtering mu')
mu_iter = iters.weighted_tau_misfit.mean() / iters.sig_n_eff.mean()
mu_real = mu_iter[(0 <= mu_iter) & (mu_iter <= 1)]

phi_iters = iters.phi.mean()
phi_keep = phi_iters[mu_real.index]


txx_keep = iters.txx.mean()[mu_real.index]
tyy_keep = iters.tyy.mean()[mu_real.index]
txy_keep = iters.txy.mean()[mu_real.index]
likelihood_keep = t_prior_df.loc[mu_real.index, 'likelihood']

fail_posteriors = pd.concat([txx_keep, tyy_keep, txy_keep, mu_real, phi_keep,
                             likelihood_keep], axis=1)

fail_posteriors.columns = ['txx','tyy','txy','mu','phi', 'likelihood']

print('Done!  saving posteriors')
fail_posteriors.to_csv(outfile, index=True)

t1 = time.time()
t_done = (t1 - t0) // 60
print(len(txx_keep))
print(t_done)

