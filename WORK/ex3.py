import numpy as np
import matplotlib.pyplot as plt

g = 10
v0 = 100
theta = np.pi/4
tmax = v0*np.sin(theta)/g
N = 100

t = np.linspace(0, tmax, N)

x = v0*np.cos(theta)*t
y = v0*np.sin(theta)*t - 0.5*g*t**2

plt.plot(x,y)
plt.show()
