# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 17:32:55 2023

@author: C.Lex
"""

"""
 A crude implementation of RK4 on the SIR compartment model for disease 
 modelling. 
 - S denotes the number of susceptible persons to the desease
 - I denotes the number of infected persons in the population
 - R denotes the number of persons no longer susceptible to the disease
 either because they are recovered from infection and immune or deceased. 
 - N is the size of the total population.
"""

import matplotlib.pyplot as plt
import pandas as pd

#The conditions for the numerical ODE-solver are assigned here
step_size = 0.01
init_val = [60000-212,8,212]
end = 20

#The model parameters are assigned here
beta = 2.33988
gamma = 1.396
N =60000

#The main algorithm
def RK4SIR(step_size, beta, gamma, N, init_val, end):
    # A list of each of the modelled variables is created.
    S = [init_val[0]]
    I = [init_val[1]]
    R = [init_val[2]]
    time = [0]
    
    #The SIR differential equations are defined as functions
    def DS(S,I,R):
        return(-beta*I*S/N)
    def DI(S,I,R):
        return(beta*I*S/N-gamma*I)
    def DR(S,I,R):
        return(gamma*I)
    
    #This function determines the weighted average RK4-slope.
    def RKslope(fun,S,I,R):
        k1 = fun(S,I,R)
        k2 = fun(S+step_size*k1/2, I+step_size*k1/2, R+step_size*k1/2)
        k3 = fun(S+step_size*k2/2, I+step_size*k2/2, R+step_size*k2/2)
        k4 = fun(S+step_size*k3, I+step_size*k3, R+step_size*k3)
        WA_slope = 1/6*(k1+2*k2+2*k3+k4)
        return(WA_slope)
    
    #The main loop where the Runge-Kutta steps are taken.
    while(time[-1] < end):
        S.append(S[-1] + RKslope(DS,S[-1],I[-1],R[-1])*step_size)
        I.append(I[-1] + RKslope(DI,S[-1],I[-1],R[-1])*step_size)
        R.append(R[-1] + RKslope(DR,S[-1],I[-1],R[-1])*step_size)
        time.append(time[-1]+step_size)
    return([time,S,I,R])

#The function is run for our parameters
res = RK4SIR(step_size, beta, gamma, N, init_val, end)

#A plot of our result. Nice!
plt.plot(res[0],res[1],res[0],res[2],res[0],res[3])



data = pd.DataFrame({"tid":res[0],"S":res[1],"I":res[2],"R":res[3]})

data.to_excel('pest.xlsx',sheet_name="sheet1",index=False)
