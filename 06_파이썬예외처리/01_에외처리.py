# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 단계에서 발생하는 예외도 중요

# 예외를 처리하는 방법은 다음과 같음.
# 1. 예외는 반드시 처리한다.
# 2. 로그로 반드시 남긴다. 
# 3. 예외를 throw 해준다.
# 4. 예외를 무시한다.

# 예외처리 기본
# try: 에러가 발생할 가능성이 있는 코드
# except 에러명: 여러 개 가능
# else: try 블록의 에러가 없을 경우 실행
# finally: 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제1
# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('Found {}. Index is {}'.format(z, x+1))
# except ValueError:
#     print('not found')
# else:
#     print('ok, else.')

# print()


# 예제2
# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('Found {}. Index is {}'.format(z, x+1))
# except Exception:
#     print('not found')
# else:
#     print('ok, else.')

# print()


# 예제 3
# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('Found {}. Index is {}'.format(z, x+1))

# # 보통 에러를 출력해준다.
# except Exception as e:
#     print(e)
#     print('not found')
# else:
#     print('ok, else.')
# finally:
#     print('ok, finally')
# print()


# 예제4
# 예외발생: raise
# raise 키워드로 예외를 직접 발생시킬 수 있음.
try:
    a = 'Park'
    if a == 'Kim':
        print('ok, pass')
    # 실제 문법적인 에러는 아니지만 문법적인 에러를 직접 발생시킬수도 있다.
    else:
        raise ValueError
except ValueError:
    print('Exception!!!')
else:
    print('ok, else')
print()