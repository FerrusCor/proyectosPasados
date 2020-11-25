# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:07:07 2019

@author: QTC
"""
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('OKDATA.txt', delimiter='\t', unpack=True)
plt.plot(x,y, color = "b")
#plt.xlabel('x')
#plt.ylabel('y')

plt.ylabel('Energía ($kcal \\, mol^{-1}$)')
plt.xlabel('Ángulo diedro ($ ^{\\circ}$)')




#plt.axis = ('off')
plt.gca().xaxis.set_major_locator(plt.MaxNLocator())
#plt.gca().yaxis.set_major_locator(plt.NullLocator())
#plt.box(False)
plt.title('Ángulo diedro $H_{2}C_{1}O_{5}H_{6}$')
#plt.savefig('C:\\Users\\QTC\\Dropbox\\Spyder UC\\Diedro.jpg',dpi=300)
plt.savefig('C:\\Users\\Francisco Burgos\\Dropbox\\Spyder UC\\Diedro.jpg',dpi=300)
plt.show()

#plt.savefig('C:\\Users\\Francisco Burgos\\Dropbox\\Spyder UC\\IRC.jpg',dpi=300)