import pandas as pd
import pyproj as pj

a = pd.read_csv('fms.csv')

wgs84 = pj.Proj(init='epsg:4326')
utm48 = pj.Proj(init='epsg:32648')

a['utm_e'], a['utm_n'] = pj.transform(wgs84, utm48,
                                      a.lon.values, a.lat.values)

a.index.name = 'id'

def get_node_strike(strike):
    ns = strike - 180
    ns[ns < 0] += 360
    
    return ns

a['strike2'] = get_node_strike(a['strike1'].values)
a['dip2'] = 90 - a.dip1

a.to_csv('wench_aftershocks.csv')
