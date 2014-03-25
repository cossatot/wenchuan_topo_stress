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


wench_slip_dir = 'multi/'
stress_f_dir = '/cmld/data7/styron/wenchuan_eq/wench_output/'

stress_file = stress_f_dir + 'e_asia_topo_stress.h5'

fs1 = wench_slip_dir + 's1_xyz.csv'
fs2 = wench_slip_dir + 's2_xyz.csv'
fs3 = wench_slip_dir + 's3_xyz.csv'
fs4 = wench_slip_dir + 's4_xyz.csv'
fs5 = wench_slip_dir + 's5_xyz.csv'

s1 = pd.read_csv(fs1, index_col=0)
s2 = pd.read_csv(fs2, index_col=0)
s3 = pd.read_csv(fs3, index_col=0)
s4 = pd.read_csv(fs4, index_col=0)
s5 = pd.read_csv(fs5, index_col=0)

# get coordinate data info (manually input)
topo_x0 = -1919052.3800296092
topo_y0 = 5429616.539854606
x_res_deg = 848.2707
y_res_deg = 848.2707

x0_conv = topo_x0
y0_conv = topo_y0 - (4343 * y_res_deg) #upper to lower edge

res_m = 848

rho = 2700
g = 9.8
depth_corr = 1000 # m in a km (depth units)
poiss_corr = 0.33 #


clip_len = 1500
clip_dist = clip_len + 1500


# make new coordinates for fault patches (in array coordinates)

s1_xyz = hbx.coord_map_inverse_3d([s1['utm_lon'],s1['utm_lat'],s1['depth_km']],
                                  x_step = x_res_deg, x_shift = x0_conv,
                                  y_step = y_res_deg, y_shift = y0_conv,
                                  z_step = 1, z_shift = 1.5)
s1_xyz = np.array(s1_xyz)
s1_xyz[0:2,:] = s1_xyz[0:2,:] - clip_len
s1_yxz = np.array([ s1_xyz[1,:], s1_xyz[0,:], s1_xyz[2,:] ])


s2_xyz = hbx.coord_map_inverse_3d([s2['utm_lon'],s2['utm_lat'],s2['depth_km']],
                                  x_step = x_res_deg, x_shift = x0_conv,
                                  y_step = y_res_deg, y_shift = y0_conv,
                                  z_step = 1, z_shift = 1.5)
s2_xyz = np.array(s2_xyz)
s2_xyz[0:2,:] = s2_xyz[0:2,:] - clip_len
s2_yxz = np.array([ s2_xyz[1,:], s2_xyz[0,:], s2_xyz[2,:] ])

s3_xyz = hbx.coord_map_inverse_3d([s3['utm_lon'],s3['utm_lat'],s3['depth_km']],
                                  x_step = x_res_deg, x_shift = x0_conv,
                                  y_step = y_res_deg, y_shift = y0_conv,
                                  z_step = 1, z_shift = 1.5)
s3_xyz = np.array(s3_xyz)
s3_xyz[0:2,:] = s3_xyz[0:2,:] - clip_len
s3_yxz = np.array([ s3_xyz[1,:], s3_xyz[0,:], s3_xyz[2,:] ])

s4_xyz = hbx.coord_map_inverse_3d([s4['utm_lon'],s4['utm_lat'],s4['depth_km']],
                                  x_step = x_res_deg, x_shift = x0_conv,
                                  y_step = y_res_deg, y_shift = y0_conv,
                                  z_step = 1, z_shift = 1.5)
s4_xyz = np.array(s4_xyz)
s4_xyz[0:2,:] = s4_xyz[0:2,:] - clip_len
s4_yxz = np.array([ s4_xyz[1,:], s4_xyz[0,:], s4_xyz[2,:] ])

s5_xyz = hbx.coord_map_inverse_3d([s5['utm_lon'],s5['utm_lat'],s5['depth_km']],
                                  x_step = x_res_deg, x_shift = x0_conv,
                                  y_step = y_res_deg, y_shift = y0_conv,
                                  z_step = 1, z_shift = 1.5)
s5_xyz = np.array(s5_xyz)
s5_xyz[0:2,:] = s5_xyz[0:2,:] - clip_len
s5_yxz = np.array([ s5_xyz[1,:], s5_xyz[0,:], s5_xyz[2,:] ])

interp_order = 1

fs = h5py.File(stress_file, 'r')

zz_stress_matrix = fs['zz_MPa']
xx_stress_matrix = fs['xx_MPa']
yy_stress_matrix = fs['yy_MPa']
xz_stress_matrix = fs['xz_MPa']
xy_stress_matrix = fs['xy_MPa']
yz_stress_matrix = fs['yz_MPa']

t1 = time.time()
print 'done in', t1 - t0, 's'

print 'calculating zz stresses at points'
zz_stress_matrix = (zz_stress_matrix[clip_len:clip_dist,
                                        clip_len:clip_dist,:])
s1_zz = nd.map_coordinates(zz_stress_matrix, s1_yxz, order = interp_order)
s2_zz = nd.map_coordinates(zz_stress_matrix, s2_yxz, order = interp_order)
s3_zz = nd.map_coordinates(zz_stress_matrix, s3_yxz, order = interp_order)
s4_zz = nd.map_coordinates(zz_stress_matrix, s4_yxz, order = interp_order)
s5_zz = nd.map_coordinates(zz_stress_matrix, s5_yxz, order = interp_order)
del zz_stress_matrix
tt0 = time.time()
print 'done in', tt0 - t1, 's'

print 'calculating xx stresses at points'
xx_stress_matrix = (xx_stress_matrix[clip_len:clip_dist,
                                        clip_len:clip_dist,:])
s1_xx = nd.map_coordinates(xx_stress_matrix, s1_yxz, order = interp_order)
s2_xx = nd.map_coordinates(xx_stress_matrix, s2_yxz, order = interp_order)
s3_xx = nd.map_coordinates(xx_stress_matrix, s3_yxz, order = interp_order)
s4_xx = nd.map_coordinates(xx_stress_matrix, s4_yxz, order = interp_order)
s5_xx = nd.map_coordinates(xx_stress_matrix, s5_yxz, order = interp_order)
del xx_stress_matrix
tt1 = time.time()
print 'done in', tt1 - tt0, 's'

print 'calculating yy stresses at points'
yy_stress_matrix = (yy_stress_matrix[clip_len:clip_dist,
                                        clip_len:clip_dist,:])
s1_yy = nd.map_coordinates(yy_stress_matrix, s1_yxz, order = interp_order)
s2_yy = nd.map_coordinates(yy_stress_matrix, s2_yxz, order = interp_order)
s3_yy = nd.map_coordinates(yy_stress_matrix, s3_yxz, order = interp_order)
s4_yy = nd.map_coordinates(yy_stress_matrix, s4_yxz, order = interp_order)
s5_yy = nd.map_coordinates(yy_stress_matrix, s5_yxz, order = interp_order)
del yy_stress_matrix
tt2 = time.time()
print 'done in', tt2 - tt1, 's'

print 'calculating xy stresses at points'
xy_stress_matrix = (xy_stress_matrix[clip_len:clip_dist,
                                        clip_len:clip_dist,:])
s1_xy = nd.map_coordinates(xy_stress_matrix, s1_yxz, order = interp_order)
s2_xy = nd.map_coordinates(xy_stress_matrix, s2_yxz, order = interp_order)
s3_xy = nd.map_coordinates(xy_stress_matrix, s3_yxz, order = interp_order)
s4_xy = nd.map_coordinates(xy_stress_matrix, s4_yxz, order = interp_order)
s5_xy = nd.map_coordinates(xy_stress_matrix, s5_yxz, order = interp_order)
del xy_stress_matrix
tt3 = time.time()
print 'done in', tt3 - tt2, 's'

print 'calculating xz stresses at points'
xz_stress_matrix = (xz_stress_matrix[clip_len:clip_dist,
                                        clip_len:clip_dist,:])
s1_xz = nd.map_coordinates(xz_stress_matrix, s1_yxz, order = interp_order)
s2_xz = nd.map_coordinates(xz_stress_matrix, s2_yxz, order = interp_order)
s3_xz = nd.map_coordinates(xz_stress_matrix, s3_yxz, order = interp_order)
s4_xz = nd.map_coordinates(xz_stress_matrix, s4_yxz, order = interp_order)
s5_xz = nd.map_coordinates(xz_stress_matrix, s5_yxz, order = interp_order)
del xz_stress_matrix
tt4 = time.time()
print 'done in', tt4 - tt3, 's'

print 'calculating yz stresses at points'
yz_stress_matrix = (yz_stress_matrix[clip_len:clip_dist,
                                        clip_len:clip_dist,:])
s1_yz = nd.map_coordinates(yz_stress_matrix, s1_yxz, order = interp_order)
s2_yz = nd.map_coordinates(yz_stress_matrix, s2_yxz, order = interp_order)
s3_yz = nd.map_coordinates(yz_stress_matrix, s3_yxz, order = interp_order)
s4_yz = nd.map_coordinates(yz_stress_matrix, s4_yxz, order = interp_order)
s5_yz = nd.map_coordinates(yz_stress_matrix, s5_yxz, order = interp_order)
del yz_stress_matrix
tt5 = time.time()
print 'done in', tt5 - tt4, 's'

fs.close()

t2 = time.time()
print 'done in', t2-t1, 's'

print 'adding results to dataframes'

s1['x_pixel'] = s1_xyz[0]
s2['x_pixel'] = s2_xyz[0]
s3['x_pixel'] = s3_xyz[0]
s4['x_pixel'] = s4_xyz[0]
s5['x_pixel'] = s5_xyz[0]

s1['y_pixel'] = s1_xyz[1]
s2['y_pixel'] = s2_xyz[1]
s3['y_pixel'] = s3_xyz[1]
s4['y_pixel'] = s4_xyz[1]
s5['y_pixel'] = s5_xyz[1]

s1['z_pixel'] = s1_xyz[2]
s2['z_pixel'] = s2_xyz[2]
s3['z_pixel'] = s3_xyz[2]
s4['z_pixel'] = s4_xyz[2]
s5['z_pixel'] = s5_xyz[2]

s1['zz_stress'] = s1_zz
s2['zz_stress'] = s2_zz
s3['zz_stress'] = s3_zz
s4['zz_stress'] = s4_zz
s5['zz_stress'] = s5_zz

s1['xx_stress'] = s1_xx
s2['xx_stress'] = s2_xx
s3['xx_stress'] = s3_xx
s4['xx_stress'] = s4_xx
s5['xx_stress'] = s5_xx

s1['yy_stress'] = s1_yy
s2['yy_stress'] = s2_yy
s3['yy_stress'] = s3_yy
s4['yy_stress'] = s4_yy
s5['yy_stress'] = s5_yy

s1['xz_stress'] = s1_xz
s2['xz_stress'] = s2_xz
s3['xz_stress'] = s3_xz
s4['xz_stress'] = s4_xz
s5['xz_stress'] = s5_xz

s1['xy_stress'] = s1_xy
s2['xy_stress'] = s2_xy
s3['xy_stress'] = s3_xy
s4['xy_stress'] = s4_xy
s5['xy_stress'] = s5_xy

s1['yz_stress'] = s1_yz
s2['yz_stress'] = s2_yz
s3['yz_stress'] = s3_yz
s4['yz_stress'] = s4_yz
s5['yz_stress'] = s5_yz


t3 = time.time()
print 'done in', t3 - t2, 's'

print 'doing norm and shear stress calcs'
s1_strike = 230 #- 90
s1_dip    = 80

s2_strike = 222 #- 90
s2_dip    = 70

s3_strike = 245 #- 90
s3_dip    = 60

s4_strike = 222 #- 90
s4_dip    = 47

s5_strike = 222 #- 90
s5_dip    = 33


s1_tens_xyz = dict([])
s2_tens_xyz = dict([])
s3_tens_xyz = dict([])
s4_tens_xyz = dict([])
s5_tens_xyz = dict([])

s1_sig_nn = dict([])
s2_sig_nn = dict([])
s3_sig_nn = dict([])
s4_sig_nn = dict([])
s5_sig_nn = dict([])

s1_tau_dd = dict([])
s2_tau_dd = dict([])
s3_tau_dd = dict([])
s4_tau_dd = dict([])
s5_tau_dd = dict([])

s1_tau_ss = dict([])
s2_tau_ss = dict([])
s3_tau_ss = dict([])
s4_tau_ss = dict([])
s5_tau_ss = dict([])

s1_tau_cs = dict([])
s2_tau_cs = dict([])
s3_tau_cs = dict([])
s4_tau_cs = dict([])
s5_tau_cs = dict([])




s1['sig_nn'] = s1['lat_deg'] - s1['lat_deg']
s1['tau_dd'] = s1['lat_deg'] - s1['lat_deg']
s1['tau_ss'] = s1['lat_deg'] - s1['lat_deg']
s1['tau_cs'] = s1['lat_deg'] - s1['lat_deg']

s2['sig_nn'] = s2['lat_deg'] - s2['lat_deg']
s2['tau_dd'] = s2['lat_deg'] - s2['lat_deg']
s2['tau_ss'] = s2['lat_deg'] - s2['lat_deg']
s2['tau_cs'] = s2['lat_deg'] - s2['lat_deg']

s3['sig_nn'] = s3['lat_deg'] - s3['lat_deg']
s3['tau_dd'] = s3['lat_deg'] - s3['lat_deg']
s3['tau_ss'] = s3['lat_deg'] - s3['lat_deg']
s3['tau_cs'] = s3['lat_deg'] - s3['lat_deg']

s4['sig_nn'] = s4['lat_deg'] - s4['lat_deg']
s4['tau_dd'] = s4['lat_deg'] - s4['lat_deg']
s4['tau_ss'] = s4['lat_deg'] - s4['lat_deg']
s4['tau_cs'] = s4['lat_deg'] - s4['lat_deg']

s5['sig_nn'] = s5['lat_deg'] - s5['lat_deg']
s5['tau_dd'] = s5['lat_deg'] - s5['lat_deg']
s5['tau_ss'] = s5['lat_deg'] - s5['lat_deg']
s5['tau_cs'] = s5['lat_deg'] - s5['lat_deg']







for i in s1.index:
    s1_tens_xyz[i] = hsp.make_xyz_stress_tensor(sig_xx = s1['xx_stress'].ix[i],
                sig_zz = s1['zz_stress'].ix[i],
                sig_yy = s1['yy_stress'].ix[i], sig_xz = s1['xz_stress'].ix[i],
                sig_xy = s1['xy_stress'].ix[i], sig_yz = s1['yz_stress'].ix[i])

    s1['sig_nn'].ix[i] = hsp.norm_stress_from_xyz(s1_strike, s1_dip,
                                                  s1_tens_xyz[i])
    s1['tau_dd'].ix[i] = hsp.dip_shear_stress_from_xyz(s1_strike, s1_dip,
                                                       s1_tens_xyz[i])
    s1['tau_ss'].ix[i] = hsp.strike_shear_stress_from_xyz(s1_strike, s1_dip,
                                                          s1_tens_xyz[i])
    s1['tau_cs'].ix[i] = hsp.coulomb_shear_stress_from_xyz(s1_strike, s1_dip,
                                                           s1_tens_xyz[i])

for i in s2.index:
    s2_tens_xyz[i] = hsp.make_xyz_stress_tensor(sig_xx = s2['xx_stress'].ix[i],
                sig_zz = s2['zz_stress'].ix[i],
                sig_yy = s2['yy_stress'].ix[i], sig_xz = s2['xz_stress'].ix[i],
                sig_xy = s2['xy_stress'].ix[i], sig_yz = s2['yz_stress'].ix[i])

    s2['sig_nn'].ix[i] = hsp.norm_stress_from_xyz(s2_strike, s2_dip,
                                                  s2_tens_xyz[i])
    s2['tau_dd'].ix[i] = hsp.dip_shear_stress_from_xyz(s2_strike, s2_dip,
                                                       s2_tens_xyz[i])
    s2['tau_ss'].ix[i] = hsp.strike_shear_stress_from_xyz(s2_strike, s2_dip,
                                                          s2_tens_xyz[i])
    s2['tau_cs'].ix[i] = hsp.coulomb_shear_stress_from_xyz(s2_strike, s2_dip,
                                                           s2_tens_xyz[i])


for i in s3.index:
    s3_tens_xyz[i] = hsp.make_xyz_stress_tensor(sig_xx = s3['xx_stress'].ix[i],
                sig_zz = s3['zz_stress'].ix[i],
                sig_yy = s3['yy_stress'].ix[i], sig_xz = s3['xz_stress'].ix[i],
                sig_xy = s3['xy_stress'].ix[i], sig_yz = s3['yz_stress'].ix[i])

    s3['sig_nn'].ix[i] = hsp.norm_stress_from_xyz(s3_strike, s3_dip,
                                                  s3_tens_xyz[i])
    s3['tau_dd'].ix[i] = hsp.dip_shear_stress_from_xyz(s3_strike, s3_dip,
                                                       s3_tens_xyz[i])
    s3['tau_ss'].ix[i] = hsp.strike_shear_stress_from_xyz(s3_strike, s3_dip,
                                                          s3_tens_xyz[i])
    s3['tau_cs'].ix[i] = hsp.coulomb_shear_stress_from_xyz(s3_strike, s3_dip,
                                                           s3_tens_xyz[i])


for i in s4.index:
    s4_tens_xyz[i] = hsp.make_xyz_stress_tensor(sig_xx = s4['xx_stress'].ix[i],
                sig_zz = s4['zz_stress'].ix[i],
                sig_yy = s4['yy_stress'].ix[i], sig_xz = s4['xz_stress'].ix[i],
                sig_xy = s4['xy_stress'].ix[i], sig_yz = s4['yz_stress'].ix[i])

    s4['sig_nn'].ix[i] = hsp.norm_stress_from_xyz(s4_strike,
                                                  s4_dip, s4_tens_xyz[i])
    s4['tau_dd'].ix[i] = hsp.dip_shear_stress_from_xyz(s4_strike, s4_dip,
                                                       s4_tens_xyz[i])
    s4['tau_ss'].ix[i] = hsp.strike_shear_stress_from_xyz(s4_strike, s4_dip,
                                                          s4_tens_xyz[i])
    s4['tau_cs'].ix[i] = hsp.coulomb_shear_stress_from_xyz(s4_strike, s4_dip,
                                                           s4_tens_xyz[i])


for i in s5.index:
    s5_tens_xyz[i] = hsp.make_xyz_stress_tensor(sig_xx = s5['xx_stress'].ix[i],
                sig_zz = s5['zz_stress'].ix[i],
                sig_yy = s5['yy_stress'].ix[i], sig_xz = s5['xz_stress'].ix[i],
                sig_xy = s5['xy_stress'].ix[i], sig_yz = s5['yz_stress'].ix[i])

    s5['sig_nn'].ix[i] = hsp.norm_stress_from_xyz(s5_strike, s5_dip,
                                                  s5_tens_xyz[i])
    s5['tau_dd'].ix[i] = hsp.dip_shear_stress_from_xyz(s5_strike, s5_dip,
                                                       s5_tens_xyz[i])
    s5['tau_ss'].ix[i] = hsp.strike_shear_stress_from_xyz(s5_strike, s5_dip,
                                                          s5_tens_xyz[i])
    s5['tau_cs'].ix[i] = hsp.coulomb_shear_stress_from_xyz(s5_strike, s5_dip,
                                                           s5_tens_xyz[i])

t4 = time.time()
print 'done in', t4-t3, 's'

print 'saving dataframes'

df1 = wench_slip_dir + 's1_stress_4km.csv'
df2 = wench_slip_dir + 's2_stress_4km.csv'
df3 = wench_slip_dir + 's3_stress_4km.csv'
df4 = wench_slip_dir + 's4_stress_4km.csv'
df5 = wench_slip_dir + 's5_stress_4km.csv'

s1.to_csv(df1)
s2.to_csv(df2)
s3.to_csv(df3)
s4.to_csv(df4)
s5.to_csv(df5)

t5 = time.time()
print 'done with everything in', t5-t0,'s'

