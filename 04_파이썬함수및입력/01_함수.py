# 함수 정의방법
# def function_name(param):
#   code


# 함수 선언
def first_function(w):
    print('Hello ' + w)

first_function('student')


def second_function(w):
    result = "Hello, " + str(w)
    return result

print(second_function('student'))


def mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return y1, y2, y3   # 여러 개의 값을 반환하는 다중반환이 가능하다.

x, y, z = mul(10)   # 물론 해당 함수의 결과값을 받을 때 여러 개의 변수를 통해 받아야 한다.

print(x, y, z)


def mul2(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return (y1, y2, y3) # tuple 형태로도 반환할 수 있다.

t = mul2(10)

print(t)


def mul3(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return [y1, y2, y3] # list 형태로도 반환할 수 있다.

l = mul3(10)

print(l)


def mul4(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return {'0': y1, '1': y2, '2': y3}    # dictionary 형태로도 반환할 수 있다.

d = mul4(10)

print(d.get('0'))
print()



# 중요
# *args, **kwargs

# *args(언팩킹)
# 어떤 시퀀스를 가지는 자료형을 매개변수로 받을 때 사용한다. ex) list, tuple, set 등
# enumerate() 함수는 시퀀스를 가지는 자료의 인덱스와 원소에 동시에 접근할 때 사용한다.
# 참고링크: https://www.daleseo.com/python-enumerate/
def args_function(*args):   # 매개변수명 자유.
    for i, v in enumerate(args):
        print('Result: {}'.format(i), v)
    print('----------------')

args_function(*[12,13,14,15])           # 해당 함수의 매개변수로 list 를 보낸다. 반드시 * 를 붙여야 한다. 
args_function(12,13,14,15)              # 위의 것과 동일한데 이렇게 여러개만 입력하면 tuple 로 인식한다. 
args_function(*('Kim', 'Lee', 'Park'))  # 직접 tuple 형태로 해줄 수도 있다. 
args_function(*{'zero', 'one', 'two'})  # 집합은 순서대로 나오지 않고 랜덤하게 나오는 것 같다. 
print()


# **kwargs(언팩킹)
# kwargs 는 keyword arguments 의 줄임말이다. 
# key-value 형태의 자료형을 매개변수로 받을 때 사용한다. 
def kwargs_function(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('----------------')

kwargs_function(**{'name1': 'Kim', 'name2': 'Lee', 'name3': 'Park'})    # dictionary 형태로 보낸다. 반드시 ** 를 붙여야 한다. 
kwargs_function(name1='Kim', name2='Lee', name3='Park')                 # 위의 것과 동일한데 형태만 다르다.
print()
print()


# 전체 혼합
def ex1(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

ex1(10, 20, 'Kim', 'Lee', 'Park', age1=20, age2=30, age3=40)    # 직접 해보면 각각 그냥 변수 2개, tuple 1개, dictionary 1개로 나오는 것을 알수있다.
print()


# 중첩함수
def parent_function(num):
    print('부모 함수가 호출되었습니다.')
    print('매개변수로 받은 값은 {} 입니다.'.format(num))
    print('자식 함수를 호출합니다.')
    def child_function(num):
        print('자식 함수가 호출되었습니다.')
        print('부모함수로부터 받은 매개변수에 100을 더한 결과는 {} 입니다.'.format(num+100))
        print('자식 함수 호출을 종료합니다.')
    child_function(num)
    print('부모 함수 호출을 종료합니다.')

parent_function(100)
print()
print()



# 람다식
# 메모리 절약, 가독성 향상, 코드 간결
# 함수 객체 생성 -> 메모리 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 감소...

a = lambda x,y: x*y     # 또 다른 변수에 할당하는 형태. JS 의 익명함수와 같다.
print(a(5,6))           

def func(func):
    print(func(100,100))
func(lambda x,y: x*y)   # 함수를 매개변수로 받는 함수를 호출할 때는 lambda 식을 사용하면 편하다.

