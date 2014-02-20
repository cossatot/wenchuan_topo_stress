import numpy as np
import pandas as pd
import halfspace.projections as hsp
import h5py

fb = pd.read_csv('../../slip_models/qi/qi_bei_rough_stress.csv', index_col=0)
fp = pd.read_csv('../../slip_models/qi/qi_peng_rough_stress.csv', index_col=0)

lms = pd.concat((fb, fp), axis=0)
lms = lms[lms.slip_m > 0]

# some inital constants
n_trials = 1e5

lms['slip_rake'] =hsp.get_rake_from_shear_components(strike_shear=lms.s_slip_m,
                                                     dip_shear=lms.d_slip_m)

lms_copy_cols = ['z_center', 'strike','dip','slip_m', 'slip_rake',
                'xx_stress', 'yy_stress', 'xy_stress', 'zz_stress',
                'xz_stress', 'yz_stress']

print('tiling lms')
lms_col_array = lms[lms_copy_cols].values
lms_reps = np.tile(lms_col_array, [n_trials, 1])

print('saving result')
f = h5py.File('qi_MC_arrays.hdf5', 'a')
f.create_dataset('qi_r_lms_tile', data=lms_reps, chunks=True)
f.close()
