# 데이터 분석에 필수!!!
# 리스트 자료형(순서있음, 중복있음, 수정가능, 삭제가능)

# 리스트 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14]
print(len(c))
print()


# 인덱싱
print(type(d), d)           # [1000, 10000, 'Ace', 'Base', 'Captain']
print(d[1])                 # 10000
print(d[0] + d[1] + d[1])   # 21000
print(d[-1])                # Captain --> index 에서 -1 은 맨 끝의 요소를 의미.
print(e[-1][1])             # Base --> e[-1] 은 ['Ace', 'Base', 'Captain'] 인데 그 중에서 index 가 1 인 요소는 Base.
print(list(e[-1][1]))       # ['B', 'a', 's', 'e'] --> 알아서 list 로 바꿔줌.
print()


# 슬라이싱
print(d[0:3])       # [1000, 10000, 'Ace']
print(d[2:])        # ['Ace', 'Base', 'Captain']
print(e[-1][1:3])   # ['Base', 'Captain']
print()


# 리스트 연산
print(c+d)                  # [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captain']
print(c*3)                  # [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
print('Test' + str(c[0]))   # Test70
print()


# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()


# Identify
temp = c
print(temp, c)
print(id(temp))
print(id(c))
print()


# 리스트 수정, 삭제 --> 슬라이싱으로 요소를 지정할때와 그냥 요소를 지정할 때의 차이
c[0] = 4
print(c)
c[1:2] = ['a', 'b', 'c']    # [['a', 'b', 'c']] 일 경우 list 안에 list 가 들어감.
print(c)
c[1] = ['a', 'b', 'c']      # list 안에 list 가 들어감. 
print(c)
c[1:3] = []
print(c)
del c[2]                    # 해당 index 의 요소 삭제
print(c)
print()


# 리스트 함수
a = [5,2,3,4,1]
print(a)
a.append(10)        # 추가
print(a)
a.sort()            # 정렬(오름차순)
print(a)
a.reverse()         # 역순
print(a)
print(a.index(10))  # 특정 요소의 index 를 출력
a.insert(2, 7)      # 특정 index 에 해당 값을 입력. 나머지는 뒤로 밀림.
print(a)
a.remove(10)        # 특정 요소 삭제
print(a)
a.pop()             # 맨 오른쪽 요소 삭제. 자료구조 중에서 stack 과 관련된 것. LIFO, FILO
print(a)
print(a.count(4))          # 특정 요소가 list 에 몇 개 있는지 반환

ex = [8,9]
a.extend(ex)               # 해당 list 의 요소들을 기존의 list 의 끝에 추가 가능.
print(a)
print()



# 삭제 --> remove, pop, del
# 반복문 활용
while a:
    data = a.pop()
    print(data)
print(a)