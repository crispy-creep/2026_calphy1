import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("seoul_temp.txt", dtype = "str")

y = data[:,3].astype("float")
x = np.arange(len(y))

plt.plot(x,y)
plt.show()