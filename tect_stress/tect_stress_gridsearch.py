import sys
sys.path.append('/cmld/data2/styron/src/halfspace/')

import numpy as np
import pandas as pd
import halfspace.projections as hsp


# Load fault slip and stress data
lms_df = pd.read_csv('../slip_models/zhang/lms_stress_slip.csv', index_col=0)

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
                  'topo_xx', 'topo_yy', 'topo_xy', 'topo_zz',
                  'topo_xz', 'topo_yz', 'slip_m', 'slip_rake',
                  'tau_rake', 'tau_mag', 'misfit', 'weighted_misfit']

search_df = pd.DataFrame(index=np.arange(len(new_index)),
                         columns=search_df_cols)

search_df[search_df_cols[:5]] = ind_array

def fill_row_vals(row, lms_df=lms_df):
    pt = row['pt_index']
    
    ser = pd.Series(index = ['topo_xx', 'topo_yy', 'topo_xy', 'topo_zz',
                             'topo_xz', 'topo_yz', 'slip_m', 'slip_rake'],
                    data = lms_df[['xx_stress', 'yy_stress', 'xy_stress',
                                   'zz_stress', 'slp_am_m','xz_stress',
                                  'yz_stress', 'rake_deg']].iloc[pt].values )
    return ser

search_df['topo_xx', 'topo_yy', 'topo_xy', 'topo_zz',
          'topo_xz', 'topo_yz', 'slip_m', 'slip_rake'] = search_df.apply(
                                                        fill_row_vals, axis=1)
 
