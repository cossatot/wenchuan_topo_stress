import pandas as pd
import numpy as np
import halfspace.projections as hsp

feng_dir = '../feng/'

feng1 = pd.read_csv(feng_dir + 'feng1_stress.csv', index_col=0)
feng2 = pd.read_csv(feng_dir + 'feng2_stress.csv', index_col=0)
feng3 = pd.read_csv(feng_dir + 'feng3_stress.csv', index_col=0)
feng4 = pd.read_csv(feng_dir + 'feng4_stress.csv', index_col=0)


