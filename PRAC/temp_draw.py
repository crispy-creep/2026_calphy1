# 라이브러리 불러오기
import numpy as np
import matplotlib.pyplot as plt

# np를 통해 txt 불러오기 
data = np.loadtxt("../seoul_temp.txt", dtype='str') 
y = data[:, 2].astype(float) # data의 3번 째 열을 불러옴
x = list(range(y.size)) # x의 사이즈를 data에서 불러옴

# pyplot을 통한 따분한 그리기.
plt.plot(x, y)
plt.title("temperature")
plt.xlabel("myamya")
plt.ylabel("temp")
plt.show()