# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:50:19 2023

@author: NRGY-chri88mh
"""

#Skrå kast med vindmodstand. Dette script giver en numerisk løsning ved 
#brug af 4. ordens Runge-Kutta-metode (RK4). 



import numpy as np
import matplotlib.pyplot as plt

#Parametre for modellen:

dragKoefficient = 0.00009
masse = 0.0002
g = 9.81

#Begyndelsesværdier:

vinkel = 0.639 
hastighed = 7.6


#Begyndelsesvektor:

begyndelsesVektor = [0 ,hastighed*np.cos(vinkel) ,0 ,hastighed*np.sin(vinkel) ]

def dx1(x1,x2,x3,x4):
    return x2
    
def dx2(x1,x2,x3,x4):
    return -(dragKoefficient/masse)*(np.sqrt(x2**2+x4**2))*x2

def dx3(x1,x2,x3,x4):
    return x4

def dx4(x1,x2,x3,x4):
    return -g -(dragKoefficient/masse)*(np.sqrt(x2**2+x4**2))*x4

def Haeldning(fun,x1,x2,x3,x4,h):
    k1 = fun(x1,x2,x3,x4)
    k2 = fun(x1+k1*h/2,x2+k1*h/2,x3+k1*h/2,x4+k1*h/2)
    k3 = fun(x1+k2*h/2,x2+k2*h/2,x3+k2*h/2,x4+k2*h/2)
    k4 = fun(x1+k3*h,x2+k3*h,x3+k3*h,x4+k3*h)
    vaegtetGns = 1/6*(k1+2*k2+2*k3+k4)
    return vaegtetGns

def RK4(begyndelse, h, ende):
    t = [0];
    x1 = [begyndelse[0]]
    x2 = [begyndelse[1]]
    x3 = [begyndelse[2]]
    x4 = [begyndelse[3]]
    while(t[-1] < ende and x3[-1]>-1.305):
        t.append(t[-1]+h)
        diff1 = Haeldning(dx1,x1[-1],x2[-1],x3[-1],x4[-1],h)
        diff2 = Haeldning(dx2,x1[-1],x2[-1],x3[-1],x4[-1],h)
        diff3 = Haeldning(dx3,x1[-1],x2[-1],x3[-1],x4[-1],h)
        diff4 = Haeldning(dx4,x1[-1],x2[-1],x3[-1],x4[-1],h)
        x1.append(diff1*h+x1[-1])
        x2.append(diff2*h+x2[-1])
        x3.append(diff3*h+x3[-1])
        x4.append(diff4*h+x4[-1])
    return x1,x2,x3,x4,t
        
x1,x2,x3,x4,t = RK4(begyndelsesVektor,0.01,3)



xData = [0,0.22,0.42,0.61,0.79,0.95,1.12,1.27,1.41,1.55,1.67,1.79,1.9,2.01,2.11,2.2,2.28,2.36,2.42,2.48,2.54,2.59,2.63,2.66,2.69,2.71,2.72]
yData = [0,0.17,0.29,0.4,0.48,0.53,0.56,0.58,0.58,0.56,0.53,0.48,0.43,0.36,0.27,0.19,0.09,-0.02,-0.14,-0.26,-0.4,-0.54,-0.67,-0.82,-0.98,-1.13,-1.3]

plt.plot(x1,x3,xData,yData)
 

