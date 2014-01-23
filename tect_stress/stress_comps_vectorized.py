import numpy as np

def strike_shear(strike=None, dip=None, rho=None, g=None, mxx=None, 
                 myy=None, mxy=None, mzz=None, myz=None, mxz=None,
                 txx=None, txy=None, tyy=None, depth=None):

    strike = np.radians(strike)
    dip = np.radians(dip)
                 
    tau_s = (-np.cos(dip)*(myz*np.cos(strike) + mxz*np.sin(strike)) 
             + np.cos(strike)*np.sin(dip)
             *((mxy + depth*g*txy*rho)*np.cos(strike) 
              + (mxx + depth*g*rho + depth*g*txx*rho)*np.sin(strike))
             -np.sin(dip)*np.sin(strike)
             *((myy + depth*g*rho +depth*g*tyy*rho)*np.cos(strike) 
              + (mxy + depth*g*txy*rho)*np.sin(strike)) )
    
    return tau_s


def dip_shear(strike=None, dip=None, rho=None, g=None, mxx=None, 
                 myy=None, mxy=None, mzz=None, myz=None, mxz=None,
                 txx=None, txy=None, tyy=None, depth=None):

    strike = np.radians(strike)
    dip = np.radians(dip)
    
    tau_d = (np.cos(strike) * np.sin(dip)
         * ((mxx + depth * g * rho + depth * g * txx * rho)
           * np.cos(dip) * np.cos(strike) 
           - (mxy + depth * g * txy * rho) * np.cos(dip) 
           * np.sin(strike) + mxz * (np.cos(strike)**2 * np.sin(dip) 
            + np.sin(dip)* np.sin(strike)**2)) 
 
         - np.sin(dip) * np.sin(strike) 
         * ((mxy + depth * g * txy * rho)
            * np.cos(dip) * np.cos(strike) 
            - (myy + depth * g * rho + depth * g * tyy * rho)
            * np.cos(dip) * np.sin(strike) + myz 
            * (np.cos(strike)**2 * np.sin(dip) + np.sin(dip) 
               * np.sin(strike)**2)) 
          -   np.cos(dip) * (mxz * np.cos(dip) * np.cos(strike) 
            - myz * np.cos(dip) * np.sin(strike) 
            + (mzz + depth * g * rho) * (np.cos(strike)**2 
                * np.sin(dip) + np.sin(dip) * np.sin(strike)**2)) )
    
    return tau_d


def eff_normal_stress(strike=None, dip=None, rho=None, g=None, mxx=None, 
                 myy=None, mxy=None, mzz=None, myz=None, mxz=None,
                 txx=None, txy=None, tyy=None, depth=None, lamb=0):

    strike = np.radians(strike)
    dip = np.radians(dip)
    
    p = rho * g * depth 
    
    s_xx = mxx + p + p * txx
    s_yy = myy + p + p * tyy
    s_zz = mzz + p
           
    p_fluid = lamb * (s_xx + s_yy + s_zz) / 3.
    
    s_xx += - p_fluid
    s_yy += - p_fluid
    s_zz += - p_fluid
    
    
    sigma_n = (-np.cos(dip) 
                 * (-s_zz * np.cos(dip) 
                    + mxz * np.cos(strike) * np.sin(dip) 
                    - myz * np.sin(dip) * np.sin(strike)) 
                 
                + np.cos(strike) * np.sin(dip) 
                 * (-mxz * np.cos(dip) + s_xx 
                    * np.cos(strike) * np.sin(dip) 
                    - (mxy + p * txy) * np.sin(dip) * np.sin(strike)) 
                 
                - np.sin(dip) * np.sin(strike) 
                * (-myz * np.cos(dip) + (mxy + p * txy) 
                   * np.cos(strike) * np.sin(dip) 
                   - s_yy * np.sin(dip) * np.sin(strike))
                )
    
    return sigma_n
