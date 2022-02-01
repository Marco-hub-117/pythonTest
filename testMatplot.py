# Semplice programma per testare l'uso della libreria matplotlib

import numpy as np 
import matplotlib.pyplot as plt

xList = []
for value in range (80, 130, 5):
	xList.append(value)

yList = []
for value in range(240,340,10):
	yList.append(value)

x = np.array(xList)
y = np.array(yList)

font1 = {'family':'serif', 'color':'blue', 'size':'20'}
font2 = {'family':'serif', 'color':'darkred', 'size':'15'}

plt.title("Sports Watch Data",fontdict = font1, loc = 'left')
plt.xlabel("Average pulse", fontdict = font2)
plt.ylabel("Calories Burnage", fontdict = font2)

plt.plot(x, y)
plt.grid() # Posso decidere di plottare solo la griglia dell'asse x (per esempio) usando plt.grid(axis = 'x')
plt.show()
