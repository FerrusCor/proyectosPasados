# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:49:30 2019

@author: Francisco Burgos
"""
import numpy
from numpy import *
import math
import matplotlib.pyplot as plt
rango = linspace(2.65,5.65,500)
a = numpy.exp
function_a = numpy.exp(-(rango-4)**2)                         #Recordar que math.exp() es e^x
function_b = numpy.exp(-(rango-1.7)**2)                       #Definimos las funciones que modelan una reacción típica
function_c = numpy.exp(-(rango-7.0)**2) 

final_function = 0.1 + (-0.4 + 1.8 * function_a + 1.2 * function_b + 0.8 * function_c)/2.3

#Axis status
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())

#Flechas
plt.annotate(s='', xy=(5.65,0.025), xytext=(5.65,0.265), arrowprops=dict(arrowstyle='<-',color="blue"))#E° Ok
#
plt.annotate(s='', xy=(3.99,0.249), xytext=(3.99,0.715), arrowprops=dict(arrowstyle='<-',color="darkgreen")) #EDDagger
#
plt.axhline(y=0.26,xmin=0.041,xmax=0.95,color="orange",linewidth=1.5,linestyle="--")

#Flechas
#plt.arrow(3.99,0.26,0,0.43,width = 0.005,head_width=0.02,head_length= 0.02,color="b")

#plt.arrow(5.65,0.03351921079432109,0,0.204,width = 0.005,head_width=0.02,head_length= 0.02,color="g")
plt.text(2.65,0.2,"R",fontsize=12) #R
plt.text(3.91,0.73,"TS",fontsize=12) #TS
plt.text(5.59,-0.02,"P",fontsize=12) #P
####TO DO{

plt.text(5.39,0.15,"$\\Delta E^{\\circ}$",fontsize=12, color="b") #Delta E°
plt.text(4.02,0.45,"$\\Delta E^{\u2260}$",fontsize=12, color="darkgreen") #Delta EDagger
plt.text(4.55,0.65,"$\\Delta E^{\u2260} = E(\\xi_{TS})-E(\\xi_{R})$",fontsize=12,color="darkgreen") #Ecuación
plt.text(4.55,0.6,"$\\Delta E^{\\circ} = E(\\xi_{P})-E(\\xi_{R})$",fontsize=12,color="b") #Ecuación
####TO DO}
plt.ylim(top=0.8,bottom=-0.1)


# Posiciones importantes en x:
# R  =  2.63         
# TS = 3.99
# P  = 5.65
plt.xticks([2.70340681,3.99,5.65],['$\\xi(R)$',"$\\xi_{TS}$","$\\xi(P)$"])    #plt.xticks([Array de valores x],[Array de strings que poner ])
plt.ylabel('Energía')
plt.xlabel('Coordenada Intrínseca de Reacción $(\\xi)$')


datos = plt.plot(rango,final_function)

#plt.box(None)
#plt.autoscale(tight=True)
#plt.tight_layout()

#plt.plot(rango,final_function)
plt.savefig('C:\\Users\\QTC\\Dropbox\\Spyder UC\\IRC.jpg',dpi=300) #Designamos la salida
#plt.savefig('C:\\Users\\Francisco Burgos\\Dropbox\\Spyder UC\\IRC.jpg',dpi=300)
plt.show()


#plt.savefig('C:\\Users\\Francisco Burgos\\Dropbox\\Spyder UC\\testdia.jpg',dpi=300,bbox_inches="tight")
