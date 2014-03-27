import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import halfspace.projections as hsp


lms = pd.read_csv('../results/zhang_tect_posteriors.csv')


XX = []
xx = []
YY = []
yy = []

for i in range(len(lms.txx)):
    X1, Y1, x1, y1 = hsp.calc_xy_princ_stresses_from_stress_comps(
                       lms.txx.values[i], lms.tyy.values[i], lms.txy.values[i])

    XX.append(X1)
    YY.append(Y1)
    xx.append(x1)
    yy.append(y1)

XX = np.array(XX)
YY = np.array(YY)
xx = np.array(xx)
yy = np.array(yy)

t_max = np.sqrt(XX**2 + YY**2)
t_min = np.sqrt(xx**2 + yy**2)


## plotting stuff

def scatter_w_marginals(x_data, y_data, c=None,
                        lw=1, s=10, alpha=1,
                        bins=10, xlabel='',
                        ylabel=''):
    
    figure()
    x_lim = (x_data.min(), x_data.max())
    y_lim = (y_data.min(), y_data.max())
    
    gs = gridspec.GridSpec(2, 2, width_ratios=[3,1],
                                 height_ratios=[1,3])
    ax = subplot(gs[1,0])
    axt = subplot(gs[0,0], sharex=ax)
    axl = subplot(gs[1,1], sharey=ax)
    
    axt.hist(x_data, bins=bins)
    axl.hist(y_data, bins=bins, orientation='horizontal')
    
    sc = ax.scatter(x_data, y_data, c=c, lw=lw, s=s, alpha=alpha)
    #colorbar(sc)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    #ax.colorbar()
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    #ylim(y_lim)
    

    
    return figure()


m_size = 2
alph  = 0.07

circ_color = 'grey'
circ_lw = 0.5

plt.figure(1)

plt.subplot(1,3,1)

rad_1 = plt.Circle((0,0), 1, color=circ_color, fill=False, lw=circ_lw)
plt.gca().add_artist(rad_1)

plt.scatter(XX, YY, c='r', s=m_size, lw=0, alpha=alph)
plt.scatter(-XX, -YY, c='r', s=m_size, lw=0, alpha=alph)
plt.axis('equal')


plt.subplot(1,3,2)

rad_1 = plt.Circle((0,0), 1, color=circ_color, fill=False, lw=circ_lw)
plt.gca().add_artist(rad_1)

plt.scatter(xx, yy, c='b', s=m_size, lw=0, alpha=alph)
plt.scatter(-xx, -yy, c='b', s=m_size, lw=0, alpha=alph)
plt.axis('equal')


plt.subplot(1,3,3)

rad_1 = plt.Circle((0,0), 1, color=circ_color, fill=False, lw=circ_lw)
plt.gca().add_artist(rad_1)

plt.scatter(XX, YY, c='r', s=m_size, lw=0, alpha=alph)
plt.scatter(-XX, -YY, c='r', s=m_size, lw=0, alpha=alph)

plt.scatter(xx, yy, c='b', s=m_size, lw=0, alpha=alph)
plt.scatter(-xx, -yy, c='b', s=m_size, lw=0, alpha=alph)

plt.axis('equal')




plt.figure(2)

plt.hist(t_max, bins=50)






plt.show()
