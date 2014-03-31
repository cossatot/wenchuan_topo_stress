import numpy as np
import pandas as pd
import stress_comps_vectorized as scv
import halfspace.projections as hsp
import time

print('getting started')
out_name = '../results/field_tect_posteriors.csv'

t0 = time.time()

lms = pd.read_csv('../../slip_models/fielding/field_topo_stress.csv',
                  index_col=0)

np.random.seed(69)

# some inital constants
n_trials = 1e5

n_points = len(lms.index)
rho = 2700
g = 9.81

# Priors for tectonic stresses (txx, tyy, txy).
# These are functions of lithostatic pressure (rho g depth)
# Priors for each are uniform [-2, 2).
s1s = np.random.uniform(0,2.5, n_trials)
s3s = np.random.uniform(0, 1, n_trials) * s1s
thetas = np.random.uniform(0, 2 * np.pi, n_trials)

xxs = scv.xx_stress_from_s1_s3_theta(s1s, s3s, thetas)
yys = scv.yy_stress_from_s1_s3_theta(s1s, s3s, thetas)
xys = scv.xy_stress_from_s1_s3_theta(s1s, s3s, thetas)

del s1s, s3s, thetas

xxs = xxs.reshape([n_trials, 1])
yys = yys.reshape([n_trials, 1])
xys = xys.reshape([n_trials, 1])

t_priors = np.concatenate((xxs, yys, xys), axis=1)

# Columns for search dataframe
search_df_cols = ['iter','txx', 'tyy', 'txy', 'pt_index', 'depth', 'strike',
                  'dip', 'slip_m', 'slip_rake']


## making index list
iter_range = np.arange(n_trials, dtype='float')
pt_range = np.arange(n_points, dtype='float')

print('making list of priors')
index_list = [[iter_range[i],t_priors[i,0],t_priors[i,1],t_priors[i,2], pi]
             for i in iter_range for pi in pt_range]
print('done making list.  Moving on...')
index_array = np.array(index_list)
del index_list

iter_index = np.int_(index_array[:,0].copy() )
pt_index = np.int_(index_array[:,4].copy() )
prior_array = index_array[:,1:4]
del index_array #save some space


# make dataframe, start filling in
print('filling in dataframe')
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

lms_copy_cols = ['z', 'strike','dip','slip', 'rake',
                'xx_stress', 'yy_stress', 'xy_stress', 'zz_stress',
                'xz_stress', 'yz_stress']

lms_col_array = lms[lms_copy_cols].values
lms_reps = np.tile(lms_col_array, [n_trials, 1])
search_df[lms_fill_cols] = lms_reps
search_df.depth *= 1000
del lms_reps

search_df[['mxx', 'myy', 'mxy', 'mzz', 'mxz', 'myz']] *= 1e6


# OK, now let's do some calculationsi
print('calculating fault stresses')
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

search_df['tau_rake'] = hsp.get_rake_from_shear_components(strike_shear=
                                                               search_df.tau_s,
                                                           dip_shear=
                                                               search_df.tau_d)

search_df['rake_misfit_rad'] = np.radians(scv.angle_difference(
                                                          search_df.slip_rake,
                                                          search_df.tau_rake,
                                                          return_abs=True) )

#search_df.to_csv('zhang_rake_search_df.csv', index=False)

sum_slip = lms.slip_m.sum()
rake_err = np.cos( np.pi/9. )

search_df['weighted_diff'] = search_df.rake_misfit_rad * search_df.slip_m


print('doing groupby')
iters = search_df.groupby('iter')
del search_df

# now define misfit function and calculate likelihood
print('calculating likelihoods')
kappa = 8.529 #calculated so that 68.2% of von mises is within pi/9 of mean

fish_l1 = iters.weighted_diff.sum() / sum_slip

fish_like = np.exp(kappa * np.cos(fish_l1) )
fish_like /= fish_like.max()

# filter by likelihood
rand_filter = np.random.random(n_trials)

fishtrap = fish_like[fish_like >= rand_filter]

iters_txx = iters.txx.mean()
iters_tyy = iters.tyy.mean()
iters_txy = iters.txy.mean()

txx_keep = iters_txx[fishtrap.index]
txy_keep = iters_txy[fishtrap.index]
tyy_keep = iters_tyy[fishtrap.index]


# done! now save files.
tect_posteriors = pd.concat([txx_keep, tyy_keep, txy_keep], axis=1,
                            names=['txx', 'tyy', 'txy'])


print('Done!  saving posteriors')
tect_posteriors.to_csv(out_name, index=False)

t1 = time.time()
t_done = t1 - t0
print('{} models out of {} ({:.2f} percent)'.format(len(txx_keep),n_trials,
                                                        float(len(txx_keep)
                                                         / n_trials) * 100) )

print(t_done)

