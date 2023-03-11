# 자주 사용하는 함수들

# 절댓값
print(abs(-3))
print()

# all(), any() --> iterable 의 요소가 참 또는 거짓인지 검사
print(all([1,2,3]))
print(all([0, 1, 2]))
print(any([0, 1, 2]))
print()


# chr(): 아스키 --> 문자, ord(): 문자 --> 아스키
print(chr(65))
print(ord('A'))
print()


# enumerate(): 인덱스 + iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

print()


# filter(함수, iterable): 반복가능한 객체요소중 지정한 함수 조건에 맞는 값 추출
print(list(filter(lambda x: abs(x) > 2, [-1, 0, 1, -3, -10])))
print()


# id(): 객체의 주소값 변환
print(id(4))
print()     


# len(): 요소의 길이 반환
print(len('hello'))
print(len([1,2,3,4,5]))
print()


# max(), min(): 최대값, 최소값
print(max([1,2,3]))
print(min([1,2,3]))
print()



# map(): 반복가능한 객체요소를 지정한 함수 실행 후 추출
print(list(map(lambda x: abs(x), [-1, -2, -3, -4, -5, -6])))
print()




# pow(): 제곱값 반환
print(pow(2, 10))
print()


# range(): 반복가능한 객체 반환
print(list(range(0, 11)))
print()


# round(): 반올림
print(round(6.5781, 2))
print()


# sorted(): 반복가능한 객체를 정렬 후 반환
print(sorted([6,5,4,3,2,1]))
print()



# sum(): 반복가능한 객체 합 반환
print(sum([1,2,3,4,5,6,7,8,9,10]))
print()


# type(): 자료형 확인
print(type(3))
print(type([]))
print()




# zip(): 반복가능한 객체의 요소를 묶어서 반환
print(list(zip([10,20,30], [40, 50, 60])))
print(list(zip([10,20,30], [40, 50])))  # 짝이 맞을경우만 zip() 실행