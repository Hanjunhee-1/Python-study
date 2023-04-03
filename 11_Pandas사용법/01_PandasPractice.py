# pandas 는 numpy 를 기반으로 처리속도가 빠르며, 행과 열을 잘 관리할 수 있는 데이터 프레임이라는 것을 제공한다.
# 설치방법: pip install pandas
import pandas as pd
import numpy as np



# 시리즈 생성하기1 (1차원 배열)
# Series() 라는 내장 함수를 통해 생성이 가능하다.

series1 = pd.Series([10, 20, 30, 40])
print(type(series1))
print(series1)
print()
print(series1[0], series1[2])   # 인덱스로 접근
print(series1.index)            # 행방향 인덱스

print()
print()
print()


# 시리즈 생성하기2
# 위의 결과를 보면 인덱스가 정수형인 것을 확인할 수 있는데 사용자가 원하는 레이블로 변경해줄수도 있다.
grades = ['A', 'B+', 'A+', 'C']
series2 = pd.Series(grades, index=['춘향', '몽룡', '향단', '방자'])
print(type(series2))
print(series2)
print()
print(series2[0], series2[2])               # 정수 인덱스로 접근
print(series2['춘향'], series2['향단'])       # 레이블로 접근
print(series2.index)                        # 인덱스 속성

print()
print()
print()


# 시리즈 생성하기3
# 사전을 이용하여 시리즈를 생성할 수도 있다.
grades = {'춘향': 'A', '몽룡': 'B+', '향단': 'A+', '방자': 'A'}
series3 = pd.Series(grades)
print(type(series3))
print(series3)
print()
print(series3[0], series3[2])               # 정수 인덱스로 접근
print(series3['춘향'], series3['향단'])      # 레이블로 접근
print()
print()
print()
print()
print()
print()


# 데이터 프레임 생성하기1 (2차원 배열)
# DataFrame() 이라는 내장 함수를 통해 생성이 가능하다. 
df1 = pd.DataFrame(np.zeros((4, 3)))    # 행이 4개, 열이 3개인 numpy array 를 생성한 후에 dataframe 으로 만들어준다.
print(type(df1))
print(df1)
print()
print()
print()


# 데이터 프레임 생성하기2 
# 바로 위의 예시에서 column 에 대한 정보가 정수인 것을 확인할 수 있는데 사용자의 기호에 따른 레이블로 바꿔줄 수 있다.
subjects = ['국어', '영어', '수학']
df2 = pd.DataFrame(np.zeros((4,3)), columns=subjects)   # 이렇게 하면 column 의 정보가 정수형이 아닌 subjects 의 요소 하나하나를 가지게 된다.
print(type(df2))
print(df2)
print()
print()
print()


# 데이터 프레임 생성하기3
# 사전과 리스트를 이용하여 데이터 프레임을 생성해줄 수 있다.
names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df3 = pd.DataFrame({'이름': names, '국어': korean, '영어': english, '수학': math})
print(type(df3))
print(df3)
print()
print()


# 데이터 프레임 사용예시1 - 열 인덱스로 시리즈 접근하기
print(df3.columns)  # 열 방향 인덱스 정보
print(df3.index)    # 행 방향 인덱스 정보
print()
name_ser = df3['이름']  # '이름' 에 대한 열의 정보들만을 가져와서 시리즈로 저장한다.
print(type(name_ser))
print(name_ser)
print()
print()
print()


# 데이터 프레임 사용예시2 - 열 인덱스를 리스트 형식으로 접근하기
subjects_df = df3[['이름', '수학']] # 열 인덱스 리스트로 접근. '이름' 과 '수학' 에 대한 열의 정보들만을 가져와서 데이터 프레임으로 저장. 여러 열을 가져오기 때문에 시리즈가 아닌 데이터 프레임으로 저장되는것!!
print(type(subjects_df))
print(subjects_df)
print()
print()
print()


# 데이터 프레임 사용예시3 - 특정 열 데이터 갱신하기
print(df3['영어'])
df3['영어'] = df3['영어'] + 10  # 모든 학생들에게 영어에 대한 보너스 점수
print(type(df3['영어']))
print(df3['영어'])
print()
print()
print()


# 데이터 프레임 사용예시4 - 행 인덱싱
# 데이터 프레임의 행인덱싱의 경우 슬라이싱을 사용해야 함.
print(df3[0:1])
print(df3[1:])
print()
print()
print()


# 데이터 프레임 사용예시5 - 개별 데이터 인덱싱
print(df3['국어'][1])       # 열을 먼저 선택한 후에 행 인덱싱
print()
print(df3[1:2]['국어'])     # 행을 먼저 선택한 후에 열 인덱싱
print()
print()
print()
print()
print()


# 데이터 프레임 행 인덱스 레이블링
df4 = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=names)    # 인덱스 정보에 대해 사용자의 기호에 맞는 레이블링을 해줄 수 있다.
print(type(df4))
print(df4)
print(df4['국어']['춘향'])  # 개별 데이터 인덱싱 활용
print()
print()
print()


# boolean 배열을 활용한 인덱싱1
bool_index = df4['수학'] > 90   # '수학' 점수가 90 점이 넘는 데이터에 대해 True 로 저장한 시리즈를 만든다.
print(type(bool_index))
print(bool_index)
print()
print(df4[bool_index])          # True 로 저장되어 있는 데이터에 대한 정보만을 출력해준다.
print()
print()
print()


# boolean 배열을 활용한 인덱싱2
bool_index = df4 > 90           # 어느 특정 열에 대한 것이 아닌 모든 데이터에 대해 True 로 저장한 데이터프레임을 만든다.
print(type(bool_index))
print(bool_index)
print()
print(df4[bool_index])
print()
print()
print()
print()
print()



# 데이터 프레임 고급 인덱싱1 - loc
print(df4)
print()
print(df4.loc['춘향'])          # 행 접근
print()
print(df4.loc[['춘향', '향단']])  # 행 리스트 접근
print()
print(df4.loc['춘향', '국어'])   # 개별 데이터 접근
print()
print()
print()

print(df4.loc['몽룡':'방자'])   # 슬라이싱인데 마지막 값까지 포함해서 반환해준다.
print()

# boolean 시리즈로 접근
print(df4.loc[df4['국어'] > 90])    # '국어' 가 90점이 넘는 모든 데이터 출력
print()

# 행과 열 모두 리스트로 접근
print(df4.loc[['춘향', '몽룡'], ['수학', '영어']])
print()

# '수학' 이 90점이 넘는 학생의 '국어' 와 '영어' 점수 출력
print(df4.loc[df4['수학'] > 90, ['국어', '영어']])
print()
print()
print()
print()
print()

# 데이터 프레임 고급 인덱싱2 - iloc
# iloc 는 loc 와 동일하지만 레이블이 아닌 정수로 인덱싱을 하는 것이다.
print(df4)
print()
print(df4.iloc[0])          # 0 번째 행 접근. 춘향에 대한 정보
print(df4.iloc[[0, 2]])     # 0 번째 행과 2 번째 행 접근. 춘향과 향단에 대한 정보
print(df4.iloc[0,0])        # 개별 데이터 접근. 춘향의 국어점수
print()
print(df4.iloc[0:2])        # 행 슬라이싱. 춘향과 몽룡에 대한 정보
print()
print(df4.iloc[0:2, 1:3])   # 행과 열 슬라이싱. 춘향과 몽룡에 대한 영어부터 수학의 점수
print()
print(df4.iloc[[0,1], [1,2]])   # 행과 열에 대해 리스트 접근. 춘향과 몽룡에 대한 영어, 수학의 점수
print()
print(df4.iloc[0] > 90)     # boolean 시리즈. 춘향이의 점수에 대해 90 점이 넘는 값은 True 로 저장.
print()
print(df4.iloc[0][df4.iloc[0] > 90])    # 행렬 인덱스 0 학생의 점수중에서 90 점이 넘는 데이터 출력. 춘향이의 점수 중 90 점이 넘는 것을 출력.
