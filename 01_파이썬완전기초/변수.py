# 기본 선언
n = 700
print(n)
print(type(n))  # 변수 타입 확인
print()


# 동시 선언
x = y = z = 700
print(x, y, z)


# 재선언
a = 75
a = 'Change Value'
print(a, type(a))
print()


# id 확인
m = 100
n = 200
print(id(m), id(n), sep='\n')
print(id(m) == id(n))
print()
n = 100
print(id(m), id(n), sep='\n')
print(id(m) == id(n))
print()