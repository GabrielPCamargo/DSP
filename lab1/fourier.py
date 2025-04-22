## LAB de Série de Fourier
import matplotlib.pyplot as plt 
import numpy as np 
f0=5
t = np.arange(0.0, 1.0, 0.001) 
x = 0 
fator=1
n=1
for temp in range(100):
 print(n)
 x=x+fator*(1/n)*np.sin(2*n*np.pi*f0*t)
 n=n+1
 plt.plot(t, x) 
 plt.show() 