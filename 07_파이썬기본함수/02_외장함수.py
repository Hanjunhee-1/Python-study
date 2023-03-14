# 실제 프로그램을 개발할 때 자주 사용
# sys, pickle, shutil, temfile, time, random 등


# 예제1
import sys
print(sys.argv)
print()

# 예제2 (강제종료)
# sys.exit()    # 아무렇게나 쓰면 위험함...


# 예제3 (파이썬 패키지 위치)
print(sys.path)
print()


# pickle: 객체 파일 쓰기
import pickle

# 예제4(쓰기)
f = open('test.obj', 'wb')
obj = {
    1: 'python',
    2: 'javascript',
    3: 'java'
}
pickle.dump(obj, f)
f.close()


# 예제5(읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
print()
f.close()


# os : 환경변수, 디렉토리(파일) 처리관련, 운영체제 작업관련
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제6
import os
print(os.environ['USERNAME'])
print()


# 예제7(현재경로)
print(os.getcwd())
print()


# time: 시간관련처리
import time

# 예제8
print(time.time())

# 예제9(형태변환)
print(time.localtime(time.time()))

# 예제10(간단표현)
print(time.ctime())

# 예제11(형식표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print()



# 예제12(시간간격발생)
# for i in range(5):
#     print(i)
#     time.sleep(1)
# print()



# random: 난수 반환
import random

# 예제13
print(random.random())  # 0~1 실수

# 예제14
print(random.randint(1, 45))    # 1~45 정수
print(random.randrange(1, 45))  # 0~44 정수
print()


# 예제15(섞기)
d = [1,2,3,4,5]
print(d)
random.shuffle(d)
print(d)
print()


# 예제16(무작위 선택)
c = random.choice(d)
print(c)
print()



# webbrowser: 본인 OS 의 웹 브라우저 실행
import webbrowser

webbrowser.open("https://google.com")
webbrowser.open_new("https://google.com")   # 새 탭에서 실행시키는 것