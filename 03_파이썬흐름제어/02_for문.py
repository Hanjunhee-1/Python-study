# for 문

for j in range(10):    # range(start, stop) 혹은 range(stop). stop 보다 하나 작은 범위까지 출력.
    print(j)
print()
for i in range(0, 10):
    print(i)
print()

for k in range(1, 11, 2):   # 1부터 10까지 나오는데 2개씩 건너뛰어서 나옴. 
    print(k)    # 1,3,5,7,9
print()


# 1 ~ 10 까지의 합
sum1 = 0
for i in range(1, 11):
    sum1 += i
print(sum1)
print()

print(sum(range(1, 11)))    # for 문을 사용하는 것보다 더 간단하게 출력가능!
print()


# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterables 를 반환하는 함수: range, reversed, enumerate, filter, map, zip
# 위의 함수는 for 문에서 사용가능!

names = {'Kim', 'Lee', 'Park', 'Choi', 'Han', 'Ahn', 'Ko'}
for name in names:
    print(name)
print()

word = 'Beautiful'
for s in word:
    print(s)
print()


info = {
    'name': 'steve',
    'age': 21,
    'city': 'Seoul'
}

for _info in info:
    print(_info)    # key: value 형태로 출력해주지 않고 key 만을 출력.
print()

for _info in info:
    print(_info, info[_info])   # value 까지도 출력해주고 싶다면 이런 식으로 가능!
print()

for val in info.values():   # values() 라는 함수가 list 를 반환하기 때문에 for 문에 사용가능
    print(val)
print()

# 모든 문자를 대문자로 만들어보기
name = 'PineApple'
for n in name:
    print(n.upper(), end='')
print()

# 굳이 대문자가 아닌 것만 대문자로 만들어주고 싶다면...
for n in name:
    if n.isupper():
        print(n, end='')
    else:
        print(n.upper(), end='')
print('\n')




# break 문
number = [14, 3, 15, 2, 90, 34, 56, 78, 90]
for n in number:
    print(n, end=' ')
    if n==34:
        break
print('\n')


# continue
# 상황설명: 문자열 타입인 것만 출력해주고 싶을때
lt = ['1', 2, '3', 4, '5', 3.14, '3.141592']
for l in lt:
    if type(l) is str:                          # 자료형을 대조할 때는 == 이 아닌 is 를 사용
        print(l, end=' ')
    else:
        continue
print('\n')




# for - else  문???
# python 에만 독보적으로 존재. if - else 구문에서 if 문이 빠지고 for 문이 들어간 형태라고 보면됨. 
for n in number:
    if n==100:
        print('찾음')
        break
else:
    print('없음')
print()



# for 문 활용
# 구구단 출력
for i in range(1, 10):
    for j in range(2, 10):
        print('{} * {} = {}'.format(j, i, i*j), end='\t')
    print()


# 뒤집어서 출력해보기
ex_str = 'AceMan'
print(''.join(list(reversed(ex_str))))  # reversed 함수는 객체의 위치를 전달해주기 때문에 다른 자료형으로 바꿔서 문자형으로 바꿔줘야 원하는대로 출력가능.
