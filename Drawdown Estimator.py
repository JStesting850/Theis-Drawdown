# This script estimated draw down in a fully confined aquifer with constant pumping
# To run the script one must provide pumping rate Q (in ft^3/d), Storativity S, Transimisivity T (ft^2/d), and time at which the curve is estimated t (days)
#import Packages
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
from scipy.special import exp1

#Define Functions
def calc_u(r,s,T,t):                #calculate and return the dimensionless time parameter,
    return r**2*S/4/T/t

def theis_drawdown(t, S, T, q, r):  #Calculate and return the drawdown s(r,t) for parameters SL, TL
    u=calc_u(r,S,T,t)
    s_theis = Q/4/np.pi/T*exp1(u)
    return s_theis

#Define variables to simulate
Q = 57750 # Pumping rate from well (f3/day)
S, T = 0.005, 2000 #Storativity (Unitless) and Transmisivity (ft2/d)
t = 1 #Drawdown calculated at time (days)

#run functions
r = np.arange(1, 2000, 1)# creates an array of distances the function will solve for (distance between 1 -> 2000 by 1)
u = calc_u(r, S, T, t)
s = theis_drawdown(t, S, T, Q, r)
s = 0-s  # reference head

#Plot
plt.plot(r,s,'b',label='300 GPM Theis Solution')
titlestring = "Estimated Drawdown After 1 Day of Pumping"
plt.title(titlestring)
plt.xlabel('Distance From Well (ft)')
plt.ylabel('Estimated Drawdown (ft)')
plt.legend()
plt.grid()
plt.show()