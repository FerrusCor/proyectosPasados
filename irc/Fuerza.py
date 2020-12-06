# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:10:33 2019

@author: QTC
"""
import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0.0, 0.25, 0.000005)
y1 = np.sin(-1*2 * np.pi * x1)

x2 = np.arange(0.25, 0.5, 0.000005)
y2 = np.sin(-1*2 * np.pi * x2)

x3 = np.arange(0.5, 0.75, 0.000005)
y3 = np.sin(-1*2 * np.pi * x3)

x4 = np.arange(0.75, 1, 0.000005)
y4 = np.sin(-1*2 * np.pi * x4)

#y4 = 1.2 * np.sin(4 * np.pi * x)



plt.arrow(0.2505,-1,0,2,color="yellow",alpha=0.5,lw=0.01)
plt.arrow(0,0,1,0,alpha=0.6,lw=0.1)






#plt.arrow(0,-1,0,2) #Izquierda
#plt.arrow(1,-1,0,2) #Derecha   ###
#plt.arrow(0,-1,1,0) #Abajo   ###
#plt.arrow(0,1,1,0) #Arriba   ###
#plt.box(on=None)
#plt.arrow(3.99,0.26,0,0.43,width = 0.001,head_width=0.02,head_length= 0.02,color="b")
###############################################################################

plt.plot(x1,y1,color="k",alpha=0.7)
plt.fill_between(x1, 0, y1,color="c")

plt.plot(x2,y2,color="k",alpha=0.7)
plt.fill_between(x2, 0, y2,color="goldenrod")

plt.plot(x3,y3,color="k",alpha=0.7)
plt.fill_between(x3, 0, y3,color="goldenrod")

plt.plot(x4,y4,color="k",alpha=0.7)
plt.fill_between(x4, 0, y4)
plt.tight_layout()
plt.fill_between(x1,-1,1,alpha=0.5,color="teal")

plt.fill_between(x2,-1,1,color="gold",alpha=0.5,lw=0)
plt.fill_between(x3,-1,1,color="gold",alpha=0.5,lw=0)
plt.fill_between(x4,-1,1,color="crimson",alpha=0.5)

##textos
w1 = plt.text(0.15,-0.5,"$W_{1}$",fontsize=12,color="w")
w2 = plt.text(0.3,-0.5,"$W_{2}$",fontsize=12,color="darkblue")
w3 = plt.text(0.65,0.5,"$W_{3}$",fontsize=12,color="darkblue")
w4 = plt.text(0.8,0.5,"$W_{4}$",fontsize=12,color="w")
#r1 = plt.text(0.03,0.70,"Región de\nReactantes",fontsize=12)
#r2 = plt.text(0.3,0.70,"Región de Estado \nde Transición",fontsize=12)
#r3 = plt.text(0.77,-0.4,"Región de\nProductos",fontsize=12)

plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())

plt.ylabel('Fuerza de Reacción')
plt.xlabel('Coordenada Intrínseca de Reacción $(\\xi)$')

plt.xticks([0,0.25,0.5,0.75,1],['$\\xi(R)$',"$\\xi_{mín}$","$\\xi_{TS}$","$\\xi_{máx}$","$\\xi(P)$"])    #plt.xticks([Array de valores x],[Array de strings que poner ])



#Agregado para cambiar el area mostrada
#plt.ylim(top=1,bottom=-3)
#plt.ylim(top=0.8,bottom=-0.1)

#ax1.set_ylabel('between y1 and 0')

plt.autoscale(tight=True)
plt.tight_layout()
#plt.savefig('C:\\Users\\QTC\\Dropbox\\Spyder UC\\Force_regiones.jpg',dpi=300,bbox_inches="tight")
plt.savefig('C:\\Users\\Francisco Burgos\\Dropbox\\Spyder UC\\Force_J.jpg',dpi=300,bbox_inches="tight")
plt.show()



