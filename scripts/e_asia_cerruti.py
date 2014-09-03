import numpy as np
import halfspace.load as hs
import time
import h5py

t0 = time.time()

#stress_dir = '/cmld/data7/styron/wenchuan_eq/wench_output/'
stress_dir = '../../stress_files/'
b_stress_file = stress_dir + 'e_asia_bouss.h5'
c_stress_file = stress_dir + 'e_asia_cerruti_topo.h5'
stress_file = stress_dir + 'e_asia_topo_stress.h5'


print 'setting up problem...'
rho = 2700  # density in kg m^-3
g = 9.81    # gravitational force in m s^-2
Fv = - rho * g
study_res = 851 # resolution for topography, filters, etc.
z_res = 1000
conv_mode = 'same'

z_min = 851.
z_max = 35851.
lame_1 = 70e9
shear_mod = 30e9
z_len = (z_max - z_min) / z_res + 1
z_vec = np.linspace(z_min, z_max, num=z_len)

kernel_rad = 9e5
kernel_len = kernel_rad * 2 / study_res +1
kernel_len = int(kernel_len)
kernel_shape = np.array( (kernel_len, kernel_len) )

print 'kernel rad', kernel_rad
print 'horiz. kernel len', kernel_len

comp_list = ['xx', 'yy', 'zz', 'xz', 'yz', 'xy']

print 'loading bouss stress arrays'
b_db = h5py.File(b_stress_file, 'r')
b_xx_top = b_db['b_xx_MPa'][:,:,0] * 1e6
b_xy_top = b_db['b_xy_MPa'][:,:,0] * 1e6
b_yy_top = b_db['b_yy_MPa'][:,:,0] * 1e6
b_shape = b_xx_top.shape

print 'loading and transforming topo...'
topo_file = ('../data/asia_clip_utm48_upright.npy')
topo = np.load(topo_file)
topo = hs._centered(topo, b_shape) * -1 # topo needs to be negative

topo_dy, topo_dx = np.gradient(topo, study_res)

print 'calculating horizontal loads'
Fh_x = b_xx_top * topo_dx + b_xy_top * topo_dy + topo * Fv * topo_dx 
Fh_y = b_yy_top * topo_dy + b_xy_top * topo_dx + topo * Fv * topo_dy

del b_xx_top, topo_dx, b_xy_top, topo_dy, b_yy_top

print 'making Cerruti output arrays'
c_x = np.zeros([topo.shape[0], topo.shape[1], z_len])
c_y = c_x.copy()
c_db = h5py.File(c_stress_file)
t_db = h5py.File(stress_file)

del topo # save some ram

cerr_x = {}
cerr_y = {}
total_dict = {}

print 'doing Cerruti calcs'
for comp in comp_list:
    print 'working on {} stresses'.format(comp)

    cerr_x[comp] = c_x.copy()
    cerr_y[comp] = c_y.copy()

    for i, z in enumerate(z_vec):
        cerr_x[comp][:,:,i] = hs.do_c_convo( component=comp, f_dir = 'x', z=z,
                                       lamb = lame_1, mu = shear_mod,
                                       load = Fh_x, kernel_res = study_res,
                                       kernel_radius = kernel_rad,
                                       conv_mode = conv_mode) * 1e-6

        cerr_y[comp][:,:,i] = hs.do_c_convo( component=comp, f_dir = 'y', z=z,
                                       lamb = lame_1, mu = shear_mod,
                                       load = Fh_y, kernel_res = study_res,
                                       kernel_radius = kernel_rad,
                                       conv_mode = conv_mode) * 1e-6

    print 'saving {} data'.format(comp)
    c_db.create_dataset('{}_x_surf_cerruti_MPa'.format(comp), 
                      data = cerr_x[comp], chunks=True, compression = 'gzip')

    c_db.create_dataset('{}_y_surf_cerruti_MPa'.format(comp), 
                      data = cerr_y[comp], chunks=True, compression = 'gzip')


    print 'adding all results together'
    total_dict[comp] = (b_db['b_{}_MPa'.format(comp)][:,:,:] + cerr_x[comp]
                        + cerr_y[comp] )

    del cerr_x[comp]
    del cerr_y[comp]
    
    t_db.create_dataset('{}_MPa'.format(comp), data=total_dict[comp],
                        chunks=True, compression='gzip')

    del total_dict[comp]

print 'done with topo corrections in', time.time() - t0, 's'

print 'closing hdf file'
b_db.close()
c_db.close()
t_db.close()

print 'done in', time.time() - t0, 's'

