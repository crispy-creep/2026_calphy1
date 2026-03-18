import numpy as np
import random

N = 1000000
Nc = 0

def f(x):
    return x**(3/2)*np.exp(-x)

for i in range(N):
    x = 3*random.random()
    y = random.random()
    if y <= f(x):
        Nc += 1

area = 3*Nc/N

print(f"area under the function = {area}")
