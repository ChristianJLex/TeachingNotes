# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 11:30:17 2023

@author: C.Lex
"""
"""
# A crude implementation of RK4 on the SIR compartment model for disease 
# modelling. 
# - S denotes the number of susceptible persons to the desease
# - I denotes the number of infected persons in the population
# - R denotes the number of persons no longer susceptible to the disease
# either because they are recovered from infection and immune or deceased. 
# - N is the size of the total population.
"""

import matplotlib.pyplot as plt


#The conditions for the numerical ODE-solver are assigned here
step_size = 0.05
init_val = [1001,1,0]
end = 15

#The model parameters are assigned here
beta = 1.5
gamma = 0.3
N = 1002

#The main algorithm
def RK4SIR(step_size, beta, gamma, N, init_val, end):
    # A list of each of the modelled variables is created.
    S = [init_val[0]]
    I = [init_val[1]]
    R = [init_val[2]]
    time = [0]
        
    while(time[-1] < end):
        #RK4 slopes for S:
        Sk1 = -beta*S[-1]*I[-1]/N
        Sk2 = -beta*(S[-1]+step_size*Sk1/2)*I[-1]/N
        Sk3 = -beta*(S[-1]+step_size*Sk2/2)*I[-1]/N
        Sk4 = -beta*(S[-1]+step_size*Sk3)*I[-1]/N
        
        #RK4 slopes for I:
        Ik1 = beta*S[-1]*I[-1]/N-gamma*I[-1]
        Ik2 = beta*S[-1]*(I[-1]+step_size*Ik1/2)/N-gamma*(I[-1]+step_size*Ik1/2)
        Ik3 = beta*S[-1]*(I[-1]+step_size*Ik2/2)/N-gamma*(I[-1]+step_size*Ik2/2)
        Ik4 = beta*S[-1]*(I[-1]+step_size*Ik1)/N-gamma*(I[-1]+step_size*Ik3)
        
        #RK4 slopes for R (R' does not depend on R; hence they are all equal):
        Rk = gamma*I[-1]
        
        #The weighted averages of the RK4-slopes:
        S_slope = 1/6*(Sk1+2*Sk2+2*Sk3+Sk4)
        I_slope = 1/6*(Ik1+2*Ik2+2*Ik3+Ik4)
        R_slope = Rk
        
        #The 
        S.append(S[-1] + S_slope*step_size)
        I.append(I[-1] + I_slope*step_size)
        R.append(R[-1] + R_slope*step_size)
        time.append(time[-1]+step_size)
    return([time,S,I,R])

#The function is run for our parameters
res = RK4SIR(step_size, beta, gamma, N, init_val, end)

#A plot of our result. Nice!
plt.plot(res[0],res[1],res[0],res[2],res[0],res[3])
