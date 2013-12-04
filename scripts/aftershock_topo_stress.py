#repo_dir = '/cmld/data2/styron/fault_elev_stress/'
#import sys
#sys.path.append(repo_dir)

import numpy as np
import pandas as pd
import scipy.ndimage as nd
import halfspace.projections as hsp
import halfspace.sandbox as hbx
import h5py
import time

t0 = time.time()
print 'setting up and scaling stress arrays...'

# import fault patches
slip_dir = '/Users/styron/topo_stress/wenchuan/slip_models/aftershocks/'
fs1 = slip_dir + 'wench_aftershocks.csv'

s1 = pd.read_csv(fs1, index_col=0)

interp_order = 1

stress_f_dir = '/Volumes/cmld/data7/styron/wenchuan_eq/wench_output/'
stress_file = stress_f_dir + 'e_asia_topo_stress.h5'
stress_db = h5py.File(stress_file, 'r')


# get coordinate data info (manually input)
topo_x0 = -1919052.3800296092
topo_y0 = 5429616.539854606
x_res_deg = 848.2707
y_res_deg = 848.2707

x0_conv = topo_x0
y0_conv = topo_y0 - (4343 * y_res_deg) #upper to lower edge

clip_len = 1500
clip_dist = clip_len + 1500

# make new coordinates for fault patches (in array coordinates)
s1_xyz = hbx.coord_map_inverse_3d([s1['utm_e'],s1['utm_n'],s1['depth']],
                                  x_step = x_res_deg, x_shift = x0_conv,
                                  y_step = y_res_deg, y_shift = y0_conv,
                                  z_step = 1, z_shift = 1.5)
s1_xyz = np.array(s1_xyz)
s1_xyz[0:2,:] = s1_xyz[0:2,:] - clip_len

comp_list = ['zz', 'xy', 'xz', 'yz', 'xx', 'yy']

print 'interpolating stresses to fault points'
for comp in comp_list:
    print 'doing {}'.format(comp)
    stress_vol = (stress_db['{}_MPa'.format(comp)][clip_len:clip_dist,
                                                   clip_len:clip_dist,:])

    s1['{}_stress'.format(comp)] = nd.map_coordinates( stress_vol,
                                    [s1_xyz[1], s1_xyz[0], s1_xyz[2]],
                                    order=interp_order)

del stress_vol                                    
stress_db.close()

print 'calculating shear and normal stresses'
s1['tau_dd_1'] = 0.
s1['tau_ss_1'] = 0.
s1['sig_nn_1'] = 0.
 
s1['tau_dd_2'] = 0.
s1['tau_ss_2'] = 0.
s1['sig_nn_2'] = 0.

stress_tens_xyz = {}

for i, fault_patch in enumerate(s1.index):
    stress_tens_xyz[i] = hsp.make_xyz_stress_tensor(
                            sig_xx = s1.xx_stress.iloc[i],
                            sig_yy = s1.yy_stress.iloc[i],
                            sig_zz = s1.zz_stress.iloc[i],
                            sig_xy = s1.xy_stress.iloc[i],
                            sig_xz = s1.xz_stress.iloc[i],
                            sig_yz = s1.yz_stress.iloc[i])

    s1['tau_dd_1'].iloc[i] = hsp.dip_shear_stress_from_xyz(
                            s1.strike1.iloc[i], s1.dip1.iloc[i],
                            stress_tens_xyz[i])
    
    s1['tau_dd_2'].iloc[i] = hsp.dip_shear_stress_from_xyz(
                            s1.strike2.iloc[i], s1.dip2.iloc[i],
                            stress_tens_xyz[i])
    
    s1['tau_ss_1'].iloc[i] = hsp.strike_shear_stress_from_xyz(
                            s1.strike1.iloc[i], s1.dip1.iloc[i],
                            stress_tens_xyz[i])
    
    s1['tau_ss_2'].iloc[i] = hsp.strike_shear_stress_from_xyz(
                            s1.strike2.iloc[i], s1.dip2.iloc[i],
                            stress_tens_xyz[i])
    
    s1['sig_nn_1'].iloc[i] = hsp.normal_stress_from_xyz(
                            s1.strike1.iloc[i], s1.dip1.iloc[i],
                            stress_tens_xyz[i])
 
    s1['sig_nn_2'].iloc[i] = hsp.normal_stress_from_xyz(
                            s1.strike2.iloc[i], s1.dip2.iloc[i],
                            stress_tens_xyz[i])
s1.to_csv(fs1)
print 'done in', time.time() - t0, 's'
