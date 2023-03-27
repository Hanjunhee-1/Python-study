# Numpy 는 계산과학분야 프로그램을 개발할 때 핵심 역할을 하는 라이브러리이다.
# Numerical Python 의 줄임말이다.
# 벡터, 행렬 등 수치 연산을 지원하고 빠른 속도로 수행됨.
# 설치방법: pip install numpy

# numpy 라이브러리를 import 해준다.
import numpy as np

# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(type(arr1))
print(arr1)
print()

# 2차원 배열 생성
arr2 = np.array([[1,2,3], [4,5,6]])
print(type(arr1))
print(arr1)
print()

# 몇 차원인지 출력하기 ndim
print(arr1.ndim)
print(arr2.ndim)

# 각 차원의 크기 shape
print(arr1.shape)
print(arr2.shape)

# 배열 요소의 자료형 확인하기 dtype
print(arr1.dtype)
print(arr2.dtype)

# 전체 요소의 개수 확인하기 size
print(arr1.size)
print(arr2.size)
print()
print()


# 0 으로 초기화된 배열 선언하기 zeros()
arr3 = np.zeros(5)          # 1차원이고 요소 5개가 0으로 초기화된 배열 선언
arr4 = np.zeros((4, 2))     # 2차원이고 요소 2개를 가지는 배열이 4개인 2차원 배열 선언


# 1.0 으로 초기화된 배열 선언하기 ones()
arr5 = np.ones(5)
print(arr5)

# ones() 의 타입을 바꿔줄 수도 있음.
arr6 = np.ones(5, dtype=int)
print(arr6)

# 연속적인 값을 가지는 배열을 생성하기 arange(초기값, 끝값, 건너뛰는 단위)
arr7 = np.arange(5)         # 0~4 까지의 값을 가지는 배열 생성
arr8 = np.arange(3, 10, 2)  # 3, 5, 7, 9 의 값을 가지는 배열 생성
print(arr7)
print(arr8)

# 차원 변경하기
arr9 = np.arange(12)            # 현재 1차원
arr10 = arr9.reshape(3, 4)      # row 가 3, column 이 4인 2차원 배열로 바꿔줌
print(arr9)
print(arr10)
arr10 = arr10.reshape(-1)       # 다차원의 배열을 다시 1차원으로 변경할 때
print(arr10)
arr10 = arr10.reshape(4, -1)    # 행의 크기만 지정하고, 열의 크기는 자율배정
print(arr10)


# numpy 배열 요소의 자료형은 무조건 같아야함.



# 다차원 인덱싱 및 슬라이싱
a = np.arange(20).reshape(4, 5)
print(a)
print()
print(a[0])             # 행 인덱싱
print(a[0][1:3])        # 특정 행에 대한 슬라이싱
print(a[2][1])          # 개별 요소 인덱싱
print()
print(a[2,1])           # 개별 요소 인덱싱
print(a[[0,2], [1,3]])  # 여려 요소 인덱싱 (0,1) 과 (2,3) 을 접근함
print()
print()
print(a)
print()
print(a[1:3])           # 행 슬라이싱
print()
print(a[1:3, 1:4])      # 행과 열 슬라이싱
print()
print(a[:, 1:3])        # 열만 슬라이싱
print()
print()
print()
print()
print()


# 실제로 사용해보기
# 학생들의 [국어, 영어, 수학] 점수가 주어졌을 때 학생별 평균을 구하라
eachStudentScores = [
    [83, 65, 57],
    [90, 71, 64],
    [84, 83, 59],
    [83, 72, 44],
    [78, 66, 67]
]

# 일단 numpy 배열로 바꿔준다.
scores = np.array(eachStudentScores)
print(scores)

# 그리고 학생이 총 몇명인지를 구한다.
num_students = scores.shape[0]  # shape 의 반환타입은 tuple 인데 (5, 3) 을 반환하게 된다. 때문에 가장 처음 것을 가져오면 그게 학생의 수가 된다.
print(num_students)

# 평균을 구해보자!
for i in range(num_students):
    print(np.mean(scores[i]))   # numpy 에서 제공해주는 함수인 mean() 함수를 통해 배열의 평균을 구할 수 있다.
print()
print()

# 그렇다면 각 학생들의 평균이 아닌 과목별 평균은 어떻게 구할까?
# 각 배열의 과목별로 슬라이싱을 해주면 될 것 같다.
num_subjects = scores.shape[1]  # 위에서 설명한 것처럼 두번째 요소가 과목수이기 때문에 이렇게 하면 된다.

for i in range(num_subjects):
    print(np.mean(scores[:, i:i+1]))    # 모든 행에 대해서 접근할 것이고 과목의 인덱스 요소에만 접근해서 np.mean() 을 사용한다.