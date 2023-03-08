# OOP (Object Oriented Programming)

# 클래스와 인스턴스의 차이를 이해하는 것이 중요
# python 에서의 클래스는 다중 생성자를 지원하지 않음... 하나의 클래스는 오로지 하나의 생성자를 가짐.

# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 접근 가능, 공유하는 변수
# 인스턴스 변수: 인스턴스마다 별도로 존재

# 클래스 생성
class Dog1(object):  # (object) 없이 해도 되고 () 만 있어도 되고 편한대로 사용.
    # 클래스 변수
    species = 'firstdog'

    # 생성자 부분. constructor 나 클래스와 동일한 이름을 사용하지 않고 python 에서는 __init__ 을 사용.
    def __init__(self, name, age):  # self 이외에 변수들은 초기화해줄 변수들  
        # 인스턴스 변수들
        self.name = name    # self 는 this 예약어와 같음
        self.age = age      # self 는 this 예약어와 같음


# 클래스의 인스턴스 생성
dog1 = Dog1('누렁이', 1)
dog2 = Dog1('백구', 2)
print(dog1.name)
print(dog2.name)

# 인스턴스의 네임스페이스 출력
print(dog1.__dict__)    # __dict__ 사용
print(dog2.__dict__)    # __dict__ 사용
print()


# self 의 이해
class SelfTest:
    def func1():
        print('func1 called')
    
    def func2(self):
        print('func2 called')

f = SelfTest()  # __init__ 이 없어도 내부적으로 알아서 생성해준다.
print(dir(f))   # 사용할 수 있는 함수 출력. func1, func2 도 있음.
# f.func1()     # 예외. 인스턴스의 id 를 넘겼는데 self 로 받아주지 않기 때문에 에러발생
f.func2()       # self 로 인스턴스의 id 를 받아주기 때문에 정상 작동

SelfTest.func1()    # 그냥 클래스로 접근하면 따로 id 값을 넘겨주지 않기 때문에 정상작동
# SelfTest.func2()  # 예외. id 값을 줘야하는데 클래스로 접근하면 id 값을 넘겨주지 않기 때문에 에러발생
SelfTest.func2(f)   # 이렇게 하면 정상작동
print()



# 클래스 변수와 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0   # 재고

    # 생성자
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        WareHouse.stock_num += 1    # 인스턴스가 생성될 때마다 재고가 1씩 증가
    
    # 소멸자
    def __del__(self):
        WareHouse.stock_num -= 1    # 인스턴스가 소멸될 때마다 재고가 1씩 감속

user1 = WareHouse('Kim')
user2 = WareHouse('Lee')
print(WareHouse.stock_num)  # stock_num = 2
print(user1.stock_num)      # 공유하기 때문에 위와 같음
print(user2.stock_num)      # 공유하기 때문에 위와 같음
print()
print(WareHouse.__dict__)   # stock_num 에 대한 정보도 나옴
print(user1.__dict__)       # stock_num 은 어처피 공유하기 때문에 안 나옴
print(user2.__dict__)       # stock_num 은 어처피 공유하기 때문에 안 나옴
print()
del user1                   # 소멸자 호출
del user2                   # 소멸자 호출
print(WareHouse.__dict__)   # stock_num 은 0으로 되어있음
print('\n')


class Dog2(object):  
    species = 'firstdog'

    def __init__(self, name, age):
        self.name = name    
        self.age = age      
    
    def show_info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def bark(self, sound):
        return '{} barked {}'.format(self.name, sound)
    
d1 = Dog2('멍멍이', 3)
print(d1.show_info())
print(d1.bark('멍멍'))


# python 에서도 이렇게 클래스를 사용할 수 있다니 좋구나