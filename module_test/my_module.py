# module: 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

def power(x, y):
    return x**y

# __name__ 을 사용한다는 것은 해당 python 파일을 외부에서 import 하여 쓸때 아래의 내용들은 작동하지 않는다는 것.
# 만약 이 파일 자체를 실행한다면 해당 내용들이 실행됨.
if __name__ == '__main__':
    print('Called __main__:')
    print(add(5,5))
    print(sub(5,5))
    print(mul(5,5))
    print(div(5,5))
    print(power(5,5))