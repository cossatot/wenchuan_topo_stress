import sys
sys.path.append('/cmld/data2/styron/src/halfspace/')

import numpy as np
import pandas as pd
import halfspace.projections as hsp
import time


# Load fault slip and stress data
lms_df = pd.read_csv('../slip_models/zhang/lms_stress_slip.csv', index_col=0)
df = lms_df
# Stress Projections

# make lists of indices
stress_step = 20
s_xx = np.arange(0, 200+stress_step, stress_step)
s_yy = np.arange(0, 200+stress_step, stress_step)
s_xy = np.arange(-50, 50+stress_step, stress_step)

tect_comp_list = [[x, y, xy] for x in s_xx for y in s_yy for xy in s_xy]
search_iter = np.arange(len(tect_comp_list))

search_index_list = [[search_iter[ii], x, y, xy] 
                   for (ii, (x, y, xy)) in enumerate(tect_comp_list)]

pt_index  = np.arange(len(lms_df.index))

new_index  = [[si, x, y, xy, pi] for (si, x, y, xy) in search_index_list
                                 for pi in pt_index]

ind_array = np.array(new_index, dtype='int')


# Make dataframe and fill in
search_df_cols = ['iter', 'tect_xx', 'tect_yy', 'tect_xy', 'pt_index',
                  'lat', 'lon', 'depth', 'strike', 'dip', 'slip_m',
                  'slip_rake', 'tau_rake', 'tau_mag', 'sig_nn', 'misfit',
                  'weighted_misfit']

search_df = pd.DataFrame(index=np.arange(len(new_index)),
                         columns=search_df_cols)

search_df[search_df_cols[:5]] = ind_array

# Make a function to fill in the row values
fill_cols = ['lat', 'lon', 'depth', 'strike', 'dip', 'slip_mag', 'slip_rake']
def fill_row_vals(row):
    pt = row['pt_index']

    s = pd.Series( data = df[['lat_deg', 'lon_deg', 'depth_km', 'strike_deg',
                              'dip_deg', 'slp_am_m', 'rake_deg']].iloc[pt],
                   index = ['lat', 'lon', 'depth', 'strike', 'dip',
                            'slip_mag', 'slip_rake'] )
    return s


print 'filling rows'
t0 = time.time()
row_chunk=1e5
chunk_min=0
chunk_max = row_chunk

search_df[fill_cols] = search_df.apply(fill_row_vals, axis=1)
t1 = time.time()
print 'done in', t1 - t0, 's'

print 'saving search_df'
search_df.to_csv('tect_search_df.csv')

print 'calculating tect stresses'
t2 = time.time()


lms_stress_cols = ['xx_stress', 'yy_stress', 'xy_stress',
                   'zz_stress', 'xz_stress', 'yz_stress']

def get_stress_tensor(row):
    pt = row['pt_index']
    (topo_xx, topo_yy, topo_xy,
     topo_zz, topo_xz, topo_yz) = lms_df[lms_stress_cols].iloc[pt]

    T = hsp.make_xyz_stress_tensor(sig_xx = topo_xx + row['tect_xx'],
                                   sig_yy = topo_yy + row['tect_yy'],
                                   sig_xy = topo_xy + row['tect_xy'],
                                   sig_zz = topo_zz, sig_xz = topo_xz,
                                   sig_yz = topo_yz)
    return T


def calc_total_stresses(row, T):
    strike = row['strike']
    dip = row['dip']

    tau_m, tau_rake = hsp.max_shear_stress_from_xyz( strike, dip, T)
    sig_nn = hsp.normal_stress_from_xyz( strike, dip, T)

    return tau_m, tau_rake, sig_nn

#def calc_row_stresses(row, df):
#    T = get_stress_tensor(row, df)

#    tau_m, tau_rake, 


def calc_misfit(row, tau_rake):

    return row['slip_rake'] - tau_rake


def calc_weighted_misfit(row, tau_rake):
    
    return (row['slip_rake'] - tau_rake) * row['slip_mag']


def do_tect_stresses(row):
    T = get_stress_tensor(row)

    tau_m, tau_rake, sig_nn = calc_total_stresses(row, T)

    misfit = calc_misfit(row, df)
    weighted_misfit = calc_weighted_misfit(row, df)

    s = pd.Series({'tau_rake':tau_rake, 'tau_mag':tau_m, 'sig_nn':sig_nn,
                   'misfit':misfit, 'weighted_misfit':weighted_misfit})

    return s

search_cols = ['tau_rake', 'tau_mag', 'sig_nn', 'misfit', 'weighted_misfit']
search_df[search_cols] = search_df.apply(do_tect_stresses, axis=1)
print 'done in', time.time() - t2, 's'

print 'saving df'
search_df.to_csv('tect_search_df.csv')
print 'done with everything in', (time.time() - t0)/60, 'min'


