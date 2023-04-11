import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=names)
print(type(df))
print(df)
print()
print()
print()
print()


# 행 추가 및 삭제
df.loc['학도'] = {'국어': 50, '영어': 50, '수학': 50}   # 행 추가
print(df)
print()
print()
print()

df.drop('학도', axis=0, inplace=True)   # axis=0 은 행 방향을 의미한다. inplace=True 는 삭제를 현재 데이터프레임 내에 반영하라는 의미
print(df)
print()
print()
print()


# 열 추가 및 삭제
df['체육'] = [100, 100, 100, 100]   # 열 추가
print(df)
print()
print()
print()
print()

df.drop('체육', axis=1, inplace=True)   # axis=1 은 열 방향을 의미한다.
print(df)
print()
print()
print()
print()