# python 에서 지원하는 자료형
'''
    int: 정수
    float: 실수
    complex: 복소수
    bool: 참/거짓
    str: 문자열(시퀀스)
    list: 리스트(시퀀스)
    tuple: 튜플(시퀀스)
    set: 집합
    dict: 사전

    *시퀀스는 연속된 무언가를 나타낸다. 순서가 나타나는 것이 특징이다.
'''


# 데이터 타입
a = "python"
b = True
c = 'Anaconda'
d = 10.0    # 10 과 10.0 은 엄연히 타입이 다르므로 같지 않다.
e = 10
f = [a, c]
g = {
    "name": "python",
    "version": 3.8
}
h = (7, 8, 9)   # 콤마로만 구분해줘도 tuple 로 인식한다.
i = {3, 5, 7}


# 데이터 타입 출력
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print()


# 숫자형 연산자
'''
    +: 덧셈
    -: 뺄셈
    *: 곱셈
    /: 나눗셈
    //: 몫만 구하기
    %: 나머지만 구하기
    abs(x): 절댓값
    pow(x, y) == x ** y: x의 y제곱
'''


# 형 변환
a = 3.0  
b = 6
c = .4  # 0 생략가능

print(type(a), type(b), type(c))
print(int(a), a)
print(int(c), c)
print(int(True), int(False))
print(complex(3))
print()


# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3))
print(5 ** 3)
print()


# 외부 모듈
import math

print(math.pi)
print(math.ceil(5.2))   # 천장함수. 해당 수보다 크거나 같은 정수를 찾음
print(math.floor(5.2))  # 바닥함수. 해당 수보다 작거나 같은 정수를 찾음
print()