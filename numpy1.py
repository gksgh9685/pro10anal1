# numpy의 ndarray는 단순한 배열이라기 보다,
# 벡터/행열 연산도 가능한 다차원 수치 데이터 구조다.
# 주요 특징 :
# 동일한 데이터 타입(homogeneous), 빠른 연산 속도, 메모리 효율성

import numpy as np
ss = ['tom', 'james', 'oscar', 1, True] # list : 여러 type의 자료로 구함
print(ss, ' ', type(ss)) # ['tom', 'james', 'oscar', 1, True] <class 'list'>

ss2 = np.array(ss)  # list type -> array type으로 변환
print(ss2, ' ', type(ss2)) # ['tom', 'james', 'oscar', 1, True] <class 'numpy.ndarra>
# 상위 type 순서 : bool -> int -> float -> complex -> str

# 메모리 비교
li = list(range(1,10))
print(li)   #[1,2,3,4,5,6,7,8,9]
print(id(li[0]),id(li[1]), hex(id(li[0])),hex(id(li[1])))
print(li * 10)  # 각 요서별 * 10이 아니라 10회 반복
print('-- ' * 10)

for i in li:
    print(i * 10, end = ' ')

print()
num_arr = np.array(li)
print(num_arr[0], ' ', num_arr[1], ' ', id(num_arr[0]), ' ', id(num_arr[1]))
# 1   2   2089913539920   2089913539920
# num_arr[0] : 배열 내부 원소를 읽어서 numpy scalar 객체로 꺼냄
print(num_arr * 10) # [10 20 30 40 50 60 70 80 90]

