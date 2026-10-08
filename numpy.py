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

