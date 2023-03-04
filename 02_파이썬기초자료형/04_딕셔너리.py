# 딕셔너리 자료형(순서없음, 키 중복 허용하지 않음, 수정가능, 삭제가능)


# 딕셔너리 선언 --> 여러가지가 존재
a = {'name': 'King'}    # key: value 형태. key 는 여러가지 자료형 가능
b = {0: 'Hello Python'}
c = {'arr': [1,2,3]}    # value 또한 어떤 형태든지 가능

d = {
    'name': 'nick',
    'city': 'Seoul',
    'age': 33,
    'grade': 'A',
    'status': True
}   #   보편적으로 모든 사람들이 아는 형식. JSON 과 같음.
print(d)

e = dict([
    ('name', 'nick'),
    ('city', 'Seoul'),
    ('age', 33),
    ('grade', 'A'),
    ('status', True)
])  #   FM 방식. 일일이 튜플로 따로 해줘야함...
print(e)

f = dict(
    name='nick',
    city='Seoul',
    age=33,
    grade='A',
    status=True
)   #   바로 위에것보다 조금 편한 방식. 보통 'd' 나 'f' 로 많이 선언한다고 함.
print(f)
print()


# 출력
print(d['name'])        # 만약 'name' 이라는 key 가 없다면 에러 발생.
print(d.get('name'))    # 만약 'name' 이라는 key 가 없다면 None 으로 출력. 좀 더 안정적!
print()


# 딕셔너리 추가
d['address'] = 'seodaemun'
print(d)
d['rank'] = [1,2,3]
print(d)
print(len(d))
print()



# 딕셔너리 keys, 딕셔너리 values, 딕셔너리 items --> 반복문에 사용가능
print(d.keys())
print(list(d.keys()))
print(d.values())
print(list(d.values()))
print(d.items())
print(list(d.items()))
print()


# 딕셔너리 삭제
print(d.pop('name'))
print(d)

print(d.popitem())  # key 와 value 를 튜플로 묶어서 한번에 제거
print(d)
print()


# in 연산자
print('name' in f)
print()


# 딕셔너리 수정
print(f)
f['name'] = 'steve'
print(f)
f.update(name='py') # 좀더 문법적인 수정.
print(f)

temp = {'name': 'python'}   # 해당 방법도 가능!
f.update(temp)
print(f)