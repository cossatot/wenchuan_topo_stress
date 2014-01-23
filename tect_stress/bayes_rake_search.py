import numpy as np
import pandas as pd
import stress_comps_vectorized as scv
import time

out_name = 'new_tect_posteriors.csv'

t0 = time.time()
lms = pd.read_csv('../slip_models/zhang/lms_stress_slip.csv', index_col=0)

# some inital constants
n_trials = 50000
n_points = len(lms.index)
rho = 2700
g = 9.81

# Priors for tectonic stresses (txx, tyy, txy).
# These are functions of lithostatic pressure (rho g depth)
# Priors for each are uniform [-2, 2).
t_priors = np.random.uniform(-2, 2, size = [n_trials,3])

# Columns for search dataframe
search_df_cols = ['iter','txx', 'tyy', 'txy', 'pt_index',
                  'depth', 'strike', 'dip', 'slip_m',
                  'slip_rake']


## making index list


iter_index = np.int_(index_array[:,0].copy() )
pt_index = np.int_(index_array[:,4].copy() )
prior_array = index_array[:,1:4]

del index_array #save some space


# make dataframe, start filling in
search_df=pd.DataFrame(index=np.arange(len(iter_index)), 
                       columns=search_df_cols, dtype=float)

search_df['iter'] = iter_index
search_df[search_df_cols[1:4]]=prior_array
search_df['pt_index'] = pt_index

search_df['mxx'] = 0.
search_df['myy'] = 0.
search_df['mxy'] = 0.
search_df['mxz'] = 0.
search_df['myz'] = 0.
search_df['mzz'] = 0.

lms_fill_cols = ['depth', 'strike', 'dip', 'slip_m', 'slip_rake',
                       'mxx', 'myy', 'mxy', 'mzz', 'mxz', 'myz']

lms_copy_cols = ['depth_km', 'strike_deg','dip_deg','slp_am_m', 'rake_deg',
                'xx_stress', 'yy_stress', 'xy_stress', 'zz_stress',
                'xz_stress', 'yz_stress']

lms_col_array = lms[lms_copy_cols].values
lms_reps = np.tile(lms_col_array, [n_trials, 1])
search_df[lms_fill_cols] = lms_reps
search_df.depth *= 1000

search_df[['mxx', 'myy', 'mxy', 'mzz', 'mxz', 'myz']] *= 1e6


# OK, now let's do some calculations
search_df['tau_s'] = scv.strike_shear(strike = search_df.strike, 
                                      dip=search_df.dip, rho=rho, g=g,
                                      mxx=search_df.mxx, myy=search_df.myy,
                                      mxy=search_df.mxy, mzz=search_df.mzz,
                                      mxz=search_df.mxz, myz=search_df.myz,
                                      txx=search_df.txx, tyy=search_df.tyy,
                                      txy=search_df.txy, depth=search_df.depth)

search_df['tau_d'] = scv.dip_shear(strike = search_df.strike, 
                                   dip=search_df.dip, rho=rho, g=g,
                                   mxx=search_df.mxx, myy=search_df.myy,
                                   mxy=search_df.mxy, mzz=search_df.mzz,
                                   mxz=search_df.mxz, myz=search_df.myz,
                                   txx=search_df.txx, tyy=search_df.tyy,
                                   txy=search_df.txy, depth=search_df.depth)

search_df['tau_rake'] = np.degrees( np.arctan2( search_df.tau_d, 
                                                search_df.tau_s) )

mean_slip = lms.slp_am_m.mean()

search_df['weighted_rake_misfit'] = (np.abs(search_df.slip_rake 
                                            - search_df.tau_rake) 
                                      * (search_df.slip_m / mean_slip) )

iters = search_df.groupby('iter')
del search_df

# now define misfit function and calculate likelihood
def l2_norm(array):
    return np.linalg.norm(array, 2)

iter_misfit = iters.weighted_rake_misfit.apply(l2_norm)

iter_likelihood = 1 / (iter_misfit / iter_misfit.min())

# filter by likelihood
rand_filter = np.random.random(n_trials)
keeps = iter_likelihood[iter_likelihood**3 >= rand_filter]

iters_txx = iters.txx.mean()
iters_tyy = iters.tyy.mean()
iters_txy = iters.txy.mean()

txx_keep = iters_txx[keeps.index]
txy_keep = iters_txy[keeps.index]
tyy_keep = iters_tyy[keeps.index]

# done! now save files.
tau_posteriors = pd.concat([txx_keep, tyy_keep, txy_keep], axis=1,
                           names=['txx', 'tyy', 'txy'])

tau_posteriors.to_csv(out_name, index=False)

t1 = time.time()
t_done = t1 - t0
print(t_done)
