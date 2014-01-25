import numpy as np
import pandas as pd
import la
import h5py

stress_f_dir = '/cmld/data7/styron/wenchuan_eq/wench_output/'
stress_file = stress_f_dir + 'e_asia_topo_stress.h5'
stress_db = h5py.File(stress_file, 'r')


# get coordinate ranges
xmin = -1919052.3800296092
ymax = 5429616.539854606
x_res_deg = 848.2707
y_res_deg = 848.2707

xmax = xmin + (5702 * x_res_deg)
ymin = ymax - (4343 * y_res_deg)

e_range = np.linspace(xmin, xmax, num=5703)
e_range = np.int_(e_range[:-1].round() )

n_range = np.linspace(ymin, ymax, num=4344)
n_range = np.int_(n_range[:-1].round() )

z_min = 851
z_max = 35851
z_len = (z_max - z_min) / 1000 + 1
z_range = np.int_( np.linspace(z_min, z_max, num=z_len) )


# make larrys
# first some intro things
stress_labels = [list(n_range), list(e_range), list(z_range)]
easting = []
northing = []

print 'doing xx stresses'
xx_la = la.larry(stress_db['xx_MPa'][:,:,:], stress_labels)

xx_sparse_5km_la = xx_la[::10, ::10, 4].flatten()

[(easting.append(e), northing.append(n)) 
  for (n, e) in xx_sparse_5km_la.label[0]]

east = pd.Series(easting)
north = pd.Series(northing)

xx_stress_vec_5 = pd.Series(xx_sparse_5km_la.x)

xx_sparse_20km_la = xx_la[::10, ::10, 20].flatten()
xx_stress_vec_20 = pd.Series(xx_sparse_20km_la.x)

xx_sparse_12km_la = xx_la[::10, ::10, 12].flatten()
xx_stress_vec_12 = pd.Series(xx_sparse_12km_la.x)

del xx_la

print 'doing yy stresses'
yy_la = la.larry(stress_db['yy_MPa'][:,:,:], stress_labels)

yy_sparse_5km_la = yy_la[::10, ::10, 4].flatten()
yy_stress_vec_5 = pd.Series(yy_sparse_5km_la.x)

yy_sparse_20km_la = yy_la[::10, ::10, 20].flatten()
yy_stress_vec_20 = pd.Series(yy_sparse_20km_la.x)

yy_sparse_12km_la = yy_la[::10, ::10, 12].flatten()
yy_stress_vec_12 = pd.Series(yy_sparse_12km_la.x)

del yy_la

print 'doing xy stresses'
xy_la = la.larry(stress_db['xy_MPa'][:,:,:], stress_labels)

xy_sparse_5km_la = xy_la[::10, ::10, 4].flatten()
xy_stress_vec_5 = pd.Series(xy_sparse_5km_la.x)

xy_sparse_20km_la = xy_la[::10, ::10, 20].flatten()
xy_stress_vec_20 = pd.Series(xy_sparse_20km_la.x)

xy_sparse_12km_la = xy_la[::10, ::10, 12].flatten()
xy_stress_vec_12 = pd.Series(xy_sparse_12km_la.x)

del xy_la

stress_db.close()

print 'making dataframes'
topo_stress_5km = pd.concat([east, north, xx_stress_vec_5, yy_stress_vec_5,
                             xy_stress_vec_5], axis=1)
topo_stress_5km.columns=['easting', 'northing', 'xx_MPa', 'yy_MPa', 'xy_MPa']

topo_stress_5km.to_csv('e_asia_horiz_stress_5km.csv', index=False)


topo_stress_12km = pd.concat([east, north, xx_stress_vec_12, yy_stress_vec_12,
                             xy_stress_vec_12], axis=1)
topo_stress_12km.columns=['easting', 'northing', 'xx_MPa', 'yy_MPa', 'xy_MPa']

topo_stress_12km.to_csv('e_asia_horiz_stress_12km.csv', index=False)


topo_stress_20km = pd.concat([east, north, xx_stress_vec_20, yy_stress_vec_20,
                             xy_stress_vec_20], axis=1)
topo_stress_20km.columns=['easting', 'northing', 'xx_MPa', 'yy_MPa', 'xy_MPa']

topo_stress_20km.to_csv('e_asia_horiz_stress_20km.csv', index=False)

