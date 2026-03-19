# 라이브러리 불러오기
import numpy as np
import matplotlib.pyplot as plt

# 초기값 정의
N = 100
x = []; y = []; theory = []; error = []; 
e_approx = 0.0

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1
    
for n in range(N):
    e_approx = e_approx + (1/factorial(n))
    x.append(n)
    y.append(e_approx)
    theory.append(np.e)
    error.append(np.abs(np.e - e_approx))

plt.plot(x, y)
plt.plot(x, theory)
plt.show()
plt.plot(x, error)
plt.show()