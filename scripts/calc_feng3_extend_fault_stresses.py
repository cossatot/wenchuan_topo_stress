import pandas as pd
import scipy.ndimage as nd
import halfspace.projections as hsp
import halfspace.sandbox as hbx
import h5py
import time
import numpy as np

t0 = time.time()


print 'setting up script'

# import fault patches

repo_dir = '/Users/styron/topo_stress/wenchuan/'
#repo_dir = '/Users/itchy/school/tibet/stress/fault_elev_stress/'
stress_file_dir = '/Volumes/cmld/data7/styron/wenchuan_eq/wench_output/'
stress_file = stress_file_dir + 'e_asia_topo_stress.h5'
interp_order = 1

feng_slip_dir = (repo_dir + 'slip_models/feng/')

fs3 = feng_slip_dir + 'f3_utm_extend.csv'

s3 = pd.read_csv(fs3, index_col=0)

s3['fault_seg'] = 's3'

#lms = pd.concat([s1, s2, s3, s4], ignore_index=True)
lms = s3.copy()

# get coordinate data info (manually input)
topo_x0 = -1919052.3800296092
topo_y0 = 5429616.539854606
x_res_deg = 848.2707
y_res_deg = 848.2707

x0_conv = topo_x0
y0_conv = topo_y0 - (4343 * y_res_deg) #upper to lower edge

clip_len = 1500
clip_dist = clip_len * 2


lms_xyz = hbx.coord_map_inverse_3d([lms['utm_lon'], lms['utm_lat'], 
                                    lms['depth']],
                                   x_step = x_res_deg, x_shift = x0_conv,
                                   y_step = y_res_deg, y_shift = y0_conv,
                                   z_step = 1, z_shift = 1.851)
lms_xyz = np.array(lms_xyz)
lms_xyz[0:2,:] = lms_xyz[0:2,:] - clip_len
lms_yxz = np.array([ lms_xyz[1,:], lms_xyz[0,:], lms_xyz[2,:] ])

print 'loading stress arrays'
fs = h5py.File(stress_file, 'r')

comp_list = ['xx', 'yy', 'zz', 'xy', 'xz', 'yz']
stress_dict = {}

for cc in comp_list:
    stress_dict[cc] = (fs['{}_MPa'.format(cc)][clip_len:clip_dist, 
                                               clip_len:clip_dist, :])

fs.close()

print 'calculating stresses at points'
lms_d = {}

for cc in comp_list:
    print 'doing', cc
    lms_d[cc] = nd.map_coordinates(stress_dict[cc], lms_yxz, order=interp_order)
    del stress_dict[cc]
    lms['{}_stress'.format(cc)] = lms_d[cc]

#print 'adding coordinate data to dataframes'
#lms['x_pixel'] = lms_xyz[0]
#lms['y_pixel'] = lms_xyz[1]
#lms['z_pixel'] = lms_xyz[2]

print 'doing normal and shear stress calculations'
lms_tens_xyz = {}

lms['sig_nn'] = 0.
lms['tau_dd'] = 0.
lms['tau_ss'] = 0.
lms['tau_cs'] = 0.

#lms['strike'] = lms['azimuth'] + 180.  # converting to right hand rule
#lms['dip'] = np.abs( lms['dip'] )
 
for i in lms.index:
    lms_tens_xyz[i] =hsp.make_xyz_stress_tensor(sig_xx = lms['xx_stress'].ix[i],
            sig_yy = lms['yy_stress'].ix[i], sig_zz = lms['zz_stress'].ix[i],
            sig_xy = lms['xy_stress'].ix[i], sig_xz = lms['xz_stress'].ix[i],
            sig_yz = lms['yz_stress'].ix[i] )
    
    lms['sig_nn'].ix[i] = hsp.norm_stress_from_xyz( lms.strike.ix[i], 
                                                 lms.dip.ix[i], lms_tens_xyz[i])

    lms['tau_dd'].ix[i] = hsp.dip_shear_stress_from_xyz( lms.strike.ix[i], 
                                                 lms.dip.ix[i], lms_tens_xyz[i])

    lms['tau_ss'].ix[i] = hsp.strike_shear_stress_from_xyz( lms.strike.ix[i], 
                                                 lms.dip.ix[i], lms_tens_xyz[i])

    lms['tau_cs'].ix[i] = hsp.coulomb_shear_stress_from_xyz( lms.strike.ix[i], 
                                                 lms.dip.ix[i], lms_tens_xyz[i])

print 'done!  now making new dataframes.'
f3 = lms[lms.fault_seg == 's3'].reset_index()

f3.to_csv(fs3)

