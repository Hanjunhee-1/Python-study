# 문자열 생성
str1 = "python"
str2 = 'python'
str3 = """Hello"""
str4 = '''World'''

# 문자열 길이 구하기
print(len(str1))    # len() 함수를 사용
print()


# 빈 문자열
empty_str1 = ''
empty_str2 = str()

print(len(empty_str1), len(empty_str2))
print()


# escape 문자사용 '\'
# I'm a boy
print('I\'m a boy') # 작은 따옴표로 묶어진 문자열에서 작은 따옴표를 표시하고 싶다면 역슬래쉬 사용
print()


# raw string 
raw_str1 = r'C:\\User'  # escape 문자를 무시.
print(raw_str1)
print()


# 다중 라인 입력 --> '\' 를 사용하면 쉽다.
multi_str1 = \
'''
다중 라인 입력 
테스트
'''
print(multi_str1)
print()


# 문자열 연산 --> 연산자 사용 가능. in 혹은 not in 으로 문자포함 하는지 판별가능
ex_str1 = 'python'
ex_str2 = 'hello'
ex_str3 = 'world'
ex_str4 = 'python is good language'

print(ex_str1 * 3)
print(ex_str1 + ex_str2)
print('y' in ex_str1)
print('z' in ex_str1)
print('p' not in ex_str2)
print()


# 문자열 형 변환 --> str() 함수를 사용했기 때문에 문자열로만 인식한다.
print(str(1), type(str(1)))
print(str(True), type(str(True)))
print()


# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha, ...)
print(ex_str1.capitalize()) # 첫글자를 대문자로 변환
print(ex_str2.endswith('o')) # 해당 글자로 끝나는지 판단
print(ex_str3.replace('wo', 'Wooooo')) # 왼쪽의 문자열을 찾아서 오른쪽 문자열로 변환
print(sorted(ex_str1)) # 해당 문자열의 각 요소를 알파벳 순(대문자 먼저) 으로 정렬하여 list 로 저장
print(ex_str4.split(' ')) # 특정 문자를 기준으로 쪼개서 list 로 저장
print()


# 반복(시퀀스) --> str 클래스에 '__iter__' 라는게 있는데 반복문을 사용할 수 있도록 해주는 클래스이다. 문자열의 각 문자 요소에 접근할 수 있다.
ex_str5 = '안녕하세요'
for i in ex_str5:
    print(i, end='! ')
print()

# 슬라이싱 --> [ 시작 : 끝 : 단위 ]
ex_str6 = 'Nice Python'
print(ex_str6[0:3]) # 0 부터 3 이전까지 나옴. 0은 생략가능
print(ex_str6[5:])  # 5 부터 끝까지
print(ex_str6[:len(ex_str6)]) # 당연히 처음부터 끝까지 나오겠지...
print(ex_str6[1:4:2]) # 1 부터 4 이전까지 나오는데 처음 나오는 1 지점부터 2 칸씩 건너뜀.
print(ex_str6[-5:]) # 문자열의 맨 오른쪽은 -1 인데 -5 지점부터 끝까지 나옴.
print(ex_str6[1:-2]) # 1 부터 -2 이전까지 나옴. -2 이전이니까 -3 지점까지 나옴.
print(ex_str6[::2]) # 처음부터 끝까지 다 나오는데 2 칸씩 건너뜀.
print(ex_str6[::-1]) # 처음부터 끝까지 다 나오는데 -1 칸씩 건너뜀. 나오는 순서가 맨 오른쪽부터 나오게됨
print()


# 아스키 코드
a = 'z'
print(ord(a)) # 해당 문자의 아스키코드 출력
print(chr(122)) # 해당 아스키코드를 가지는 문자출력