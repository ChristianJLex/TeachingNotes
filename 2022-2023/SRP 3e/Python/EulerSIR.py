# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 11:31:02 2023

@author: NRGY-chri88mh
"""

import numpy as np
import matplotlib.pyplot as plt


step_size = 0.05
init_val = [1001,1,0]
end = 15
beta = 1.5
gamma = 0.7
N = 1002

def EulerSIR(step_size, beta, gamma, N, init_val, end):
    S = [init_val[0]]
    I = [init_val[1]]
    R = [init_val[2]]
    time = [0]
    while(time[-1] < end):
        S.append((-beta*I[-1]*S[-1]/N)*step_size+ S[-1])
        I.append((beta*I[-1]*S[-1]/N-gamma*I[-1])*step_size +I[-1])
        R.append((gamma*I[-1])*step_size+R[-1])
        time.append(time[-1]+step_size)
    return([S,I,R,time])

res = EulerSIR(step_size,beta,gamma,N,init_val,end)



plt.plot(res[3],res[0],res[3],res[1],res[3],res[2])