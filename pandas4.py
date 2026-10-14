# dataframe의 재구조화(열을 행으로, 행을 열로 ...)
import numpy as np
import pandas as pd

df = pd.DataFrame(1000 + np.arange(6).reshape(2,3), index=['대전','서울'],columns=['2023','2024','2025'])
print(df)

print()
# stack, unstack
df_row = df.stack() # 열을 아래로 내려서 행 인덱스 쪽으로 쌓기
print(df_row)
print()
df_col = df_row.unstack() # 행 인덱스를 다시 열쪽으로 펼치기
print(df_col)

print('\n범주화 ----')
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]
result_cut = pd.cut(price, cut) # 연속형 -> 범주형
print(result_cut)   # 범주화 ----[(9, 11], (3, 7], (7, 9], (3, 7]]

result_cut = pd.cut(price, bins=cut, labels=['저가','중가','고가'])
print(result_cut)
print(pd.Series(result_cut).value_counts())

# pd.qcut() : 데이터 계수가 비슷하도록 분위수 기분 자동 분할

print('-----')
datas = pd.Series(np.arange(1, 1001))
# print(datas)
print(datas[:5])
print(datas.head()) # 상동
print(datas.head(2))

print(datas[-2:])
print(datas.tail(2)) #상동

print('\nagg 함수 : 범주의 그룹별 연산')
datas = pd.DataFrame({
    '부서':['개발','개발','영업','영업','인사','개발'],
    '이름' :['길동','철수','영희','민수','유리','찬우'],
    '연봉' :[4500,4200,4000,4600,3500,3900],
    '성과점수':[90,85,70,75,88,95]
})
print(datas)

print()
print(datas.groupby('부서')['연봉'].mean()) # 부서별 연봉 평균
print(datas.groupby('부서')['이름'].count()) # 부서별 건수
print(datas.groupby('부서')[['연봉','성과점수']].mean()) # 부서별 연봉,성과점수 평균

pd.set_option('display.max_columns',None)
print(datas.groupby('부서')['연봉'].agg(['sum','mean','count'])) # 여러 집계합, 평균, 건수

print()
# agg 대신 사용자 함수를 작성

data = pd.DataFrame({
    '연봉' :[4500,4200,4000,4600,3500,3900],
    '성과점수':[90,85,70,75,88,95]
})

def summaryFunc(gr):
    return{
        'count':gr.count(),
        'mean':gr.mean(),
        'std':gr.std(),
        'min':gr.min(),
    }

print(data.apply(summaryFunc)) # apply : 함수를 실행하는 함수
