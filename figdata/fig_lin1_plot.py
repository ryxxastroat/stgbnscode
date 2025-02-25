import numpy as np
import matplotlib.pyplot as plt
from numpy import log10 as lg
from numpy import pi as pi
from scipy.interpolate import interp1d as sp_interp1d
from scipy.integrate import odeint
from scipy.integrate import ode
import warnings
import timeit
import scipy.optimize as opt
from matplotlib import cm
from astropy import constants as const
from astropy import units as u
plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] = 25
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.size'] = 8
plt.rcParams['ytick.major.size'] = 8
plt.rcParams['xtick.minor.size'] = 4
plt.rcParams['ytick.minor.size'] = 4
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['axes.labelpad'] = 8.0
plt.rcParams['figure.constrained_layout.h_pad'] = 0
plt.rcParams['text.usetex'] = True
plt.rc('text', usetex=True)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.tick_params(axis='both', which='minor', labelsize=18)
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import sys
import warnings
import timeit
import numpy as np
import scipy.optimize
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.integrate import ode as sp_ode
import math

t0 = timeit.time.time()
from shapely.geometry import LineString
from scipy.interpolate import UnivariateSpline
from matplotlib.legend_handler import HandlerTuple



class HandlerTupleVertical(HandlerTuple):
    def __init__(self, **kwargs):
        HandlerTuple.__init__(self, **kwargs)

    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # How many lines are there.
        numlines = len(orig_handle)
        handler_map = legend.get_legend_handler_map()

        # divide the vertical space where the lines will go
        # into equal parts based on the number of lines
        height_y = (height / numlines)

        leglines = []
        for i, handle in enumerate(orig_handle):
            handler = legend.get_legend_handler(handler_map, handle)

            legline = handler.create_artists(legend, handle,
                                             xdescent,
                                             (2*i + 1)*height_y,
                                             width,
                                             2*height,
                                             fontsize, trans)
            leglines.extend(legline)

        return leglines
        
        
        
G=const.G.cgs.value
c=const.c.cgs.value
MSUN=const.M_sun.cgs.value
hbar=const.hbar.cgs.value
m_n=const.m_n.cgs.value
KM=10**5


G=const.G.cgs.value
c=const.c.cgs.value
Ms=const.M_sun.cgs.value
hbar=const.hbar.cgs.value
m_n=const.m_n.cgs.value
km=10**5


label=['WFF1','SLy4','AP4', 'MPA1','PAL1']

PI4 = 4.0 * pi
ka = 8.0 * pi
c = 29979245800.0  # cm/s
G = 6.67408e-8  # cm^3/g/s^2

MSUN = 1.98855e33  # g
KM = 1.0e5  # cm
mB = 1.660538921e-24  # g
E_NUCL = 2.0e14  # minimun energy density for NS core; g/cm^3

runit = 10.*KM # length to parametrize quantities

def rdiml(r):
    """ dimensionless mass """
    return r/runit    
def mdiml(m):
    """ dimensionless mass """
    return G*m/c**2/runit
def pdiml(p):
    """ dimensionless pressure """
    return G*p/c**4 * runit**2

colorset = ['black', 'lightcoral','yellowgreen']  


stdata1 = np.genfromtxt('stgb_linear_sol_data1.txt')
stdata2 = np.genfromtxt('stgb_linear_sol_data2.txt')
stdata3 = np.genfromtxt('stgb_linear_sol_data3.txt')
stdata4 = np.genfromtxt('stgb_linear_sol_data4.txt')
stdata5 = np.genfromtxt('stgb_linear_sol_data5.txt')
stdata6 = np.genfromtxt('stgb_linear_sol_data6.txt')

stn1 = len(stdata1)
#stn1, stn2, stn3, stn4, stn5 = len(strot1), len(strot2), len(strot3), len(strot4), len(strot5)
ntrim = 900

# ec, interior ph_r/ph, exterior ph_r/ph
d10, d11, d12 = stdata1[:, 0], stdata1[:, 1]/10, stdata1[:, 2]/10
d20, d21, d22 = stdata2[:, 0], stdata2[:, 1]/10, stdata2[:, 2]/10
d30, d31, d32 = stdata3[:, 0], stdata3[:, 1]/10, stdata3[:, 2]/10
d40, d41, d42 = stdata4[:, 0], stdata4[:, 1]/10, stdata4[:, 2]/10
d50, d51, d52 = stdata5[:, 0], stdata5[:, 1]/10, stdata5[:, 2]/10
d60, d61, d62 = stdata6[:, 0], stdata6[:, 1]/10, stdata6[:, 2]/10


fig, (ax1,ax2) = plt.subplots(2, 1,figsize=(10,12),sharex=True)
plt.subplots_adjust(hspace=0.0)






# ax1.set_xlabel(r'$\epsilon_0$', fontsize=20)
ax1.set_ylabel(r'$\Phi^{\prime}/\Phi|_{ s}\,[\rm \,km^{-1}]$', fontsize=30)
ax2.set_xlabel(r'$\epsilon_0/c^{2}\,[10^{15}\,\rm g\,\rm cm^{-3}]$', fontsize=30)
ax2.set_ylabel(r'$\Phi^{\prime}/\Phi|_{ s}\,[\rm \,km^{-1}]$', fontsize=30)


 
# ph_r/ph
ax1.set_ylim([-1.1, 1.1])
#ax1.set_xlim([0, 10])
p1, = ax1.plot( d40[0:ntrim]/10**15, d41[0:ntrim] , '--', color = colorset[0],linewidth=2)
p2, = ax1.plot( d40[0:ntrim]/10**15, d42[0:ntrim] , color = colorset[0],linewidth=2)


p3, = ax1.plot( d50[0:ntrim]/10**15, d51[0:ntrim] , '--', color = colorset[1],linewidth=2)
p4, = ax1.plot( d50[0:ntrim]/10**15, d52[0:ntrim] , color = colorset[1],linewidth=2)
line1=LineString(np.column_stack((d50/10**15,d51)))
line2=LineString(np.column_stack((d50/10**15,d52)))
intersection=line1.intersection(line2)

ax1.plot(*intersection.xy,color=colorset[1], markersize=10,marker='o')
p5, = ax1.plot( d60[0:ntrim]/10**15, d61[0:ntrim] , '--', color = colorset[2],linewidth=2)
# a=np.zeros(900)
# b=np.zeros(900)


# find the jump location
for i in range(1,ntrim):
    if abs(d62[i]-d62[i-1])>10:
        a=d60[i]
        b=i

p6, = ax1.plot(d60[0:b-1]/10**15, d62[0:b-1] , color = colorset[2],linewidth=2)
ax1.plot(d60[b+1:ntrim]/10**15, d62[b+1:ntrim] , color = colorset[2],linewidth=2)
line1=LineString(np.column_stack((d60[b+1:ntrim]/10**15,d61[b+1:ntrim])))
line2=LineString(np.column_stack((d60[b+1:ntrim]/10**15,d62[b+1:ntrim])))
intersection=line1.intersection(line2)
ax1.plot(*intersection.xy, colorset[2], markersize=10,marker='o')
# line1=LineString(np.column_stack((d60/10**15,d61)))
# line2=LineString(np.column_stack((d60/10**15,d62)))
# intersection=line1.intersection(line2)
# if intersection.geom_type == 'MultiPoint':
#     ax1.plot(*LineString(intersection).xy, 'o')
# elif intersection.geom_type == 'Point':
#     plt.plot(*intersection.xy, 'o')

line1=LineString(np.column_stack((d60[0:b-1]/10**15,d61[0:b-1])))
line2=LineString(np.column_stack((d60[0:b-1]/10**15,d62[0:b-1])))
intersection=line1.intersection(line2)
ax1.plot(*intersection.xy ,colorset[2], markersize=10,marker='o')


ax2.set_ylim([-1.1, 1.1])
#ax1.set_xlim([0, 10])
q1, = ax2.plot( d10[0:ntrim]/10**15, d11[0:ntrim] , '--', color = colorset[0],linewidth=2)
q2, = ax2.plot( d10[0:ntrim]/10**15, d12[0:ntrim] , color = colorset[0],linewidth=2)

for k in range(1,ntrim):
    if abs(d21[k]-d21[k-1])>50:
        e=d20[k]
        f=k
q3, = ax2.plot( d20[0:f-1]/10**15, d21[0:f-1] , '--', color = colorset[1],linewidth=2)
ax2.plot( d20[f+1:ntrim]/10**15, d21[f+1:ntrim] , '--', color = colorset[1],linewidth=2)
q4, = ax2.plot( d20[0:ntrim]/10**15, d22[0:ntrim] , color = colorset[1],linewidth=2)

line1=LineString(np.column_stack((d20[0:f-1]/10**15, d21[0:f-1])))
line2=LineString(np.column_stack((d20[0:f-1]/10**15, d22[0:f-1])))
intersection=line1.intersection(line2)
ax2.plot(*intersection.xy, color=colorset[1], markersize=10,marker='o')


# find the jump location
c=[]
d=[]
for i in range(1,ntrim):
    if abs(d31[i]-d31[i-1])>10:
        c.append(d31[i])
        d.append(i)
    
q5, = ax2.plot( d30[0:439]/10**15, d31[0:439] , '--', color = colorset[2],linewidth=2)
ax2.plot( d30[446:635]/10**15, d31[446:635] , '--', color = colorset[2],linewidth=2)
ax2.plot( d30[640:787]/10**15, d31[640:787] , '--', color = colorset[2],linewidth=2)
ax2.plot( d30[788:ntrim]/10**15, d31[788:ntrim] , '--', color = colorset[2],linewidth=2)
# ax2.plot( d30[0:ntrim]/10**15, d31[0:ntrim] , '--', color = colorset[2],linewidth=2)
q6, = ax2.plot( d30[0:ntrim]/10**15, d32[0:ntrim] , color = colorset[2],linewidth=2)

line1=LineString(np.column_stack((d30[0:439]/10**15, d31[0:439])))
line2=LineString(np.column_stack((d30[0:439]/10**15, d32[0:439])))
intersection=line1.intersection(line2)
ax2.plot(*intersection.xy, color=colorset[2], markersize=10,marker='o')

line1=LineString(np.column_stack((d30[446:635]/10**15, d31[446:635])))
line2=LineString(np.column_stack((d30[446:635]/10**15, d32[446:635])))
intersection=line1.intersection(line2)
ax2.plot(*intersection.xy, color=colorset[2], markersize=10,marker='o')

line1=LineString(np.column_stack((d30[640:787]/10**15, d31[640:787])))
line2=LineString(np.column_stack((d30[640:787]/10**15, d32[640:787])))
intersection=line1.intersection(line2)
ax2.plot(*intersection.xy, color=colorset[2], markersize=10,marker='o')




plt.xlim(min(d10)/10**15,d10[ntrim]/10**15)
ax1.minorticks_on()
ax2.minorticks_on()
# print( '\n *** STG_solver uses %.2f seconds\n' % (timeit.time.time() - t0))
ax1.legend([(p1, p2), (p3, p4), (p5, p6)], ['$b=0.9$', '$b=3$', '$b=10$'],
               handler_map={tuple: HandlerTupleVertical()}, fontsize=20,frameon=False)
ax2.legend([(q1, q2), (q3, q4), (q5, q6)], ['$b=-0.04$', '$b=-0.2$', '$b=-1$'],
               handler_map={tuple: HandlerTupleVertical()}, fontsize=20,frameon=False, loc='upper right')
#ax1.legend(fontsize=20,frameon=False)
#ax2.legend(fontsize=20,frameon=False,loc='upper right')
plt.savefig("fig_lin1.pdf", format='pdf', bbox_inches="tight")
plt.show()
