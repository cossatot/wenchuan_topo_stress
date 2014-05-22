print('importing modules')

import numpy as np
import pandas as pd
import stress_comps_vectorized as scv
import h5py

print('reading dataframes')
fb = pd.read_csv('../../slip_models/qi/qi_bei_smooth_stress.csv', index_col=0)
fp = pd.read_csv('../../slip_models/qi/qi_peng_smooth_stress.csv', index_col=0)

lms = pd.concat((fb, fp), axis=0)
lms = lms[lms.slip_m > 0]

# some inital constants
n_trials = 1e5
np.random.seed(69)

n_points = len(lms.index)
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

iter_range = np.arange(n_trials, dtype='float')
pt_range = np.arange(n_points, dtype='float')

print('making list of priors')
index_list = [[iter_range[i],t_priors[i,0],t_priors[i,1],t_priors[i,2], pi]
             for i in iter_range for pi in pt_range]
print('done making list.  Moving on...')
index_array = np.array(index_list)
del index_list
#np.save('qi_index_array_1e5.npy', index_array)

print('saving file to hdf')
f = h5py.File('qi_MC_arrays.hdf5', 'a')
f.create_dataset('qi_s_index_array', data=index_array, chunks=True)
f.close()
