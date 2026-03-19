# 라이브러리 불러오기
import numpy as np
import matplotlib.pyplot as plt

# 초기값 설정
g = 10
theta = 20*np.pi/180
v0 = 100
tmax = 2*v0*np.sin(theta)/g

# 매개변수 초기화
t = np.linspace(0, tmax, 100)

# 정의역 및 치역 설정
x = v0*np.cos(theta)*t
y = v0*np.sin(theta)*t- 0.5*g*t**2

# 따분한 그리기.
plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()