# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 11:08:53 2023

@author: NRGY-chri88mh
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(x,y):
    return(1/(2*np.sqrt(x)))

def realfun(x):
    return(np.sqrt(x))

step_size = 1
init_val = [1,1]
end = 5


def RK4(step_size, function, init_val, end):
    x = [init_val[0]]
    y = [init_val[1]]
    while(x[-1] < end):
        k1 = function(x[-1],y[-1])
        k2 = function(x[-1]+step_size/2,y[-1]+step_size*(k1/2))
        k3 = function(x[-1]+step_size/2,y[-1]+step_size*(k2/2))
        k4 = function(x[-1]+step_size,y[-1]+step_size*k3)
        WA_slope = 1/6*(k1+2*k2+2*k3+k4)
        y.append(y[-1]+WA_slope*step_size)
        x.append(x[-1]+step_size)
    return([x,y])

res = RK4(step_size,fun,init_val,end)

Real = np.linspace(init_val[0],end,1000)



plt.plot(res[0],res[1],Real,realfun(Real))
