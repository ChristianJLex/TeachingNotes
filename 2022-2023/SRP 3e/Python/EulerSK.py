# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:53:49 2023

@author: NRGY-chri88mh
"""

#Skrå kast med vindmodstand. Dette script giver en numerisk løsning ved 
#brug af Eulers metode. 


import numpy as np
import matplotlib.pyplot as plt

#Parametre for modellen:

dragKoefficient = 0.00009
masse = 0.0002
g = 9.81

#Begyndelsesværdier:

vinkel = 0.639 
hastighed = 7.99

#Begyndelsesvektor:

begyndelsesVektor = [0 ,hastighed*np.cos(vinkel) ,0 ,hastighed*np.sin(vinkel) ]

def haeldning(x):
    xmaerke1 = x[1]
    xmaerke2 = -(dragKoefficient/masse)*np.sqrt(x[1]**2+x[3]**2)*x[1]
    xmaerke3 = x[3]
    xmaerke4 = -g-(dragKoefficient/masse)*np.sqrt(x[1]**2+x[3]**2)*x[3]
    return [xmaerke1,xmaerke2,xmaerke3,xmaerke4]

def Euler(begyndelse, h, ende):
    t = [0]
    x1 = [begyndelse[0]]
    x2 = [begyndelse[1]]
    x3 = [begyndelse[2]]
    x4 = [begyndelse[3]]
    while(t[-1] < ende):
        t.append(t[-1]+h)
        diff = haeldning([x1[-1],x2[-1],x3[-1],x4[-1]])
        x1.append(diff[0]*h+x1[-1])
        x2.append(diff[1]*h+x2[-1])
        x3.append(diff[2]*h+x3[-1])
        x4.append(diff[3]*h+x4[-1])
    return x1,x2,x3,x4,t

x1,x2,x3,x4,t = Euler(begyndelsesVektor,0.001,1)

xData = [0,0.22,0.42,0.61,0.79,0.95,1.12,1.27,1.41,1.55,1.67,1.79,1.9,2.01,2.11,2.2,2.28,2.36,2.42,2.48,2.54,2.59,2.63,2.66,2.69,2.71,2.72]
yData = [0,0.17,0.29,0.4,0.48,0.53,0.56,0.58,0.58,0.56,0.53,0.48,0.43,0.36,0.27,0.19,0.09,-0.02,-0.14,-0.26,-0.4,-0.54,-0.67,-0.82,-0.98,-1.13,-1.3]

plt.plot(x1,x3,xData,yData)

        
        
        
