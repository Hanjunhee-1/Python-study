# 기본 출력
print('Python Start');
print("Python Start");
print('''Python Start''');
print("""Python Start""");
# 따옴표와 큰따옴표를 3번사용해서 묶어줘도 된다!!


# separator 옵션 사용
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',');
print('010', '1234', '5678', sep='-');
# 문자나 문자열 중간에 separator 를 넣어준다.


# end 옵션 사용
print('Welcome to', end='\n')
print('Python World')
'''
    end 옵션을 사용하지 않으면 자동으로 줄바꿈이 되지만 end 옵션을 사용한다면
    해당 변수를 출력하고 끝에 end 옵션에 저장된 값이 출력된다. 
'''


# format 사용 (d, s, f)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format(1, 2))
'''
    C 언어에서 출력해주던 것처럼 %s, %d, %f 를 통해 각 타입에 맞게 출력해줄 수 있다.
    python 에서는 format() 이라는 것을 지원해주는데 사용법은 다음과 같다.
        
        1. 먼저 {} 을 통해 format() 의 매개변수가 들어갈 자리를 정해준다.
        2. 어느 타입이든 적어서 출력한다.

    %s 에는 문자열, %d 에는 정수, %f 에는 실수가 들어간다면 format() 을 사용하면
    아무타입이나 들어갈 수 있다.

    뿐만 아니라 {} 안에 숫자를 넣어줄 수도 있는데 해당 숫자는 format() 의 매개변수의
    index 즉, 순서를 의미한다. 
'''


# %s 사용
print('%10s' % ('nice'))                # 10자리를 맞춰서 출력. 왼쪽은 공백
print('{:>10}'.format('nice'))          # 위와 같음

print('%-10s' % ('nice'))               # 10자리를 맞춰서 출력. 오른쪽은 공백
print('{:10}'.format('nice'))           # 위와 같음

print('{:_>10}'.format('nice'))         # 10자리를 맞춰서 출력. 왼쪽은 공백이 아닌 언더바.
print('{:^10}'.format('nice'))          # 10자리를 맞추고 글자를 가운데 정렬

print('%.5s' % ('nice'))                # 5자리만 맞춰서 출력해줌.
print('%.5s' % ('pythonstudy'))         # 5자리가 넘어가면 5자리까지만 출력해줌.
print('{:10.5}'.format('pythonstudy'))  # 5자리까지만 출력해주긴하는데 공간은 10자리 확보.


# %d 사용 (중괄호 안에도 d 를 명시해줘야함.)
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))         # 4자리 맞춰서 출력. 왼쪽 공백
print('{:4d}'.format(42))   # 위와 같음.


# %f 사용 (중괄호 안에도 d 를 명시해줘야함.)
print('%f' % (3.14141414141414))
print('{:f}'.format(3.141414141414))



# 숫자 단위 자동 separator
# fstring 을 사용.
m = 1000000000

print(f'm: {m:,}')