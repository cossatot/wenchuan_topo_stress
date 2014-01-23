import numpy as np
from stress_comps_vectorized import strike_shear, dip_shear, eff_normal_stress 


# test numbers

rho = 2700
g = 9.81

txx =              -0.532378
tyy =               0.091610
txy =              -0.171124
depth =          1969.600000
strike =          230.000000
dip =              80.000000
mxx =        10976253.429215
myy =        30172522.971082
mxy =         1070610.613817
mxz =         1869992.542014
myz =         2392968.966096
mzz =        19372076.331012

mc_xx = txx * rho * g * depth + mxx + rho * g * depth
mc_yy = tyy * rho * g * depth + myy + rho * g * depth
mc_xy = txy * rho * g * depth + mxy
mc_zz = mzz + rho * g * depth
mc_xz = mxz
mc_yz = myz


# test result values are from analogous halfspace.projection results, rounded

def test_dip_shear():
    ds = dip_shear(strike=strike, dip=dip, rho=rho, g=g,
             mxx=mxx, myy=myy, mxy=mxy, mzz=mzz,
             mxz=mxz, myz=myz, txx=txx, tyy=tyy, 
             txy=txy, depth=depth)

    ds = np.int( np.round(ds) )

    assert ds == 924052, 'dip shear stress'


def test_strike_shear():
    ss = strike_shear(strike=strike, dip=dip, rho=rho, g=g,
             mxx=mxx, myy=myy, mxy=mxy, mzz=mzz,
             mxz=mxz, myz=myz, txx=txx, tyy=tyy, 
             txy=txy, depth=depth)

    ss = np.int( np.round(ss) )

    assert ss == -23234845, 'dip shear stress'


def test_normal_stress_dry():
    snd = eff_normal_stress(strike=strike, dip=dip, rho=rho, g=g,
             mxx=mxx, myy=myy, mxy=mxy, mzz=mzz,
             mxz=mxz, myz=myz, txx=txx, tyy=tyy, 
             txy=txy, depth=depth, lamb=0)

    snd = np.int( np.round( snd) )

    assert snd == 73202216, 'dry normal stress'


def test_normal_stress_wet():
    snw = eff_normal_stress(strike=strike, dip=dip, rho=rho, g=g,
             mxx=mxx, myy=myy, mxy=mxy, mzz=mzz,
             mxz=mxz, myz=myz, txx=txx, tyy=tyy, 
             txy=txy, depth=depth, lamb=0.4)

    snw = np.int( np.round( snw) )

    assert snw == 47331163, 'wet normal stress'

