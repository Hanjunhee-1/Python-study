# if 문 예시 --> indent(들여쓰기) 가 중요. python 은 모든 문법에서 {} 를 따로 사용하지 않고 indent 로 구분함.
if True:
    print('Good')
if False:
    print('Bad')

if False:
    print('Bad2')
else:
    print('Good2')
print()


# 관계 연산자
# >, >=, <, <=, ==, !=

x = 15
y = 15

if x==y:
    print('same')
elif x>y:
    print('x greater than y')
else:
    print('y greater than x')
print()


city = ''
if not city:                    # JS 에서는 !city 이런 식으로 했다면 python 에서는 not city 로 사용함.
    print('city is empty')
else:
    print(city)
print()


# 논리연산자
# and, or, not
a = 100
b = 90
c = 80

print(a > b and b > c)
print(b > a or b > c)
print(not a < c)
print()



# 여러 조건 확인하기
if a == 100 and b >= 90:
    print('pass')
print()


# 중첩 if 문
grade = 'A'
total = 89

if grade == 'A':
    if total >= 90:
        print('전액 장학금')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')
print()


# in, not in 연산자
q = [10,  20, 30]
w = {70, 80, 90, 100}
e = {'name': 'steve', 'city': 'Seoul', 'grade': 'A'}
r = (10, 12, 14)

print(15 in q)
print(70 not in w)
print('name' in e)      # key 값에 대해서만 판별
print('steve' in e.values())     # values() 를 통해 value 값에 대해서도 판별하는 것이 가능