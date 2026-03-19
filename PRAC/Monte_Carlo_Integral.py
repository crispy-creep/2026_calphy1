# 라이브러리 불러오기
import numpy as np
import random


# 초기값 설정
N = 1000000
Nc = 0

# x is in (-1,1), y is in (-1, 1)인 정사각형에 임의의 점 찍기
for i in range(N):
    x = 2*random.random() - 1
    y = 2*random.random() - 1
    # 만약 원 내부에 점이 찍히면 count
    if x**2 + y**2 <= 1:
        Nc += 1
# 원/사각형 비율을 numerical하게 구함
ration = Nc/N
# 원의 면적을 구하고 변수를 정의함
area = 4*ration

# 따분한 출력
print(f"area in circle = {area}")