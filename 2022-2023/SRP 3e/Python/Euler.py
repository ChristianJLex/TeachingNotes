# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 09:45:04 2023

@author: NRGY-chri88mh
"""

#Crude implementation of Euler's Method for numerically solving ODE's

import numpy as np
import matplotlib.pyplot as plt

def fun(x,y):
    return(2*x)

def realfun(x):
    return(x**2)

step_size = 0.05
init_val = [1,1]
end = 3


def Euler(step_size, function, init_val, end):
    x = [init_val[0]]
    y = [init_val[1]]
    while(x[-1] < end):
        y.append(y[-1]+function(x[-1],y[-1])*step_size)
        x.append(x[-1]+step_size)
    return([x,y])

res = Euler(step_size,fun,init_val,end)

Real = np.linspace(init_val[0],end,1000)



plt.plot(res[0],res[1],Real,realfun(Real))


