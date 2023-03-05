# 집합 특 --> 순서없음, 중복허용하지 않음, 추가가능, 삭제가능

# 집합 선언
a = set()
b = set([1,2,3,4])
print(b)
c = set([1, 2, 'pen'])
print(c)
d = {'foo', 'bar', 'baz', 'foo'} # 집합은 중복을 허용하지 않기 때문에 중복된 값을 넣었다면 그 중 하나만 출력됨
print(d)
print()


# 집합을 튜플로 set --> tuple
t = tuple(b)
print(t)
print(type(t))
print()


# 집합을 리스트로 set --> list
l = list(c)
print(l)
print(type(l))
print()



# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)              # 교집합
print(s1.intersection(s2))  # 교집합

print(s1 | s2)              # 합집합
print(s1.union(s2))         # 합집합

print(s1 - s2)              # 차집합
print(s1.difference(s2))    # 차집합
print()


# 집합에서 중복 원소 확인
print(s1.isdisjoint(s2))    # 결과값이 false 일때 중복 원소가 존재한다는 것.
print()


# 부분 집합 확인
print({1,2,3}.issubset(s1))     # {1,2,3} 이 s1 의 부분집합인지 확인.
print(s1.issuperset({1,2,3}))   # s1 이 {1,2,3} 의 상위집합인지 확인.
print()


# 집합 추가와 제거
s3 = set([1,2,3,4])
s3.add(5)           # 기존 집합에 5 추가
print(s3)
s3.remove(5)        # 기존 집합에서 5 삭제
s3.discard(4)       # 기존 집합에서 4 삭제
print(s3)
s3.clear()          # 집합의 모든 내용 삭제
print(s3)