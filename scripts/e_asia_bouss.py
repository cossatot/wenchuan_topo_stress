repo_dir = '/cmld/data2/styron/fault_elev_stress/'
import sys
sys.path.append(repo_dir)

import numpy as np
import halfspace.load as hs
import halfspace.sandbox as hbx
import scipy.fftpack as sf
import time
import h5py

stress_dir = '/cmld/data7/styron/wenchuan_eq/wench_output/'
stress_file = stress_dir + 'e_asia_bouss.h5'

print 'setting up problem...'
rho = 2700  # density in kg m^-3
g = 9.81    # gravitational force in m s^-2
Fv =  -rho * g
study_res = 851 # resolution for topography, filters, etc.
z_res = 1000
b_conv_mode = 'valid'

z_min = 851
z_max = 35851
z_len = (z_max - z_min) / z_res + 1
z_vec = np.linspace(z_min, z_max, num=z_len)

kernel_rad = 9e5
kernel_len = kernel_rad * 2 / study_res +1
kernel_len = int(kernel_len)
kernel_shape = np.array( (kernel_len, kernel_len) )

print 'kernel rad', kernel_rad
print 'horiz. kernel len', kernel_len


print 'loading and transforming topo...'
t0 = time.time()
topo_file = (repo_dir + 'data/asia_clip_utm48_upright.npy')
#topo_fft_file = repo_dir + 'data/e_asia_utm48_851m_up_fft.npy'
topo = np.load(topo_file)
topo_shape = np.array(topo.shape)

topo = hs._centered(topo, topo_shape - 2000) * -1 # elevs need to be negative
topo_shape = np.array(topo.shape)
#topo_shape = np.array([8458, 9817])
size = kernel_shape + topo_shape -1
fsize = 2 **(np.ceil( np.log2( size) ) )

topo_fft = sf.fftn(topo, fsize)
del topo

t1 = time.time()
print 'done in', t1 - t0, 's'


print 'setting up matrices...'
b_out_x, b_out_y = hbx.size_output(kernel_shape, topo_shape, mode =b_conv_mode)
b_out_size = np.array( (b_out_x, b_out_y, z_len ) )
b_stress = np.empty( (b_out_size) )

t2 = time.time()
print 'done in', t2 - t1, 's'

d = h5py.File(stress_file)
b_dict = {}
comp_list = ['zz', 'xy', 'xz', 'yz'] #'xx', 'yy'] 


for comp in comp_list:
    print 'working on {} stresses'.format(comp)
    b_dict[comp] = b_stress.copy()

    for i, z in enumerate(z_vec):
       b_dict[comp][:,:,i] = hs.do_b_convo( component = comp,  z = z, Fv = Fv,
                                        load = topo_fft, load_mode = 'fft',
                                        conv_mode = b_conv_mode, size = size,
                                        kernel_radius = kernel_rad,
                                        kernel_res = study_res)

    b_dict[comp] *= 1e-6  # scale results to MPa
    
    d.create_dataset('b_{}_MPa'.format(comp), data = b_dict[comp],
                     chunks = True, compression = 'gzip')

    del b_dict[comp]

print 'done with Boussinesq calcs in', time.time() - t2, 's'

print 'closing hdf file'
d.close()
