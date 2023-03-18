# 읽기모드(r), 쓰기모드(w), 추가모드(a), 텍스트모드(t), 바이너리모드(b)
# 추가모드는 append 의 a 를 따온것이다.


# 파일읽기(read)
# 예제1
f = open('./readTest/test1.txt', 'rt', encoding='UTF-8') # 텍스트 모드로 읽겠다. 텍스트 모드는 default 이므로 굳이 안써도 무관

# 속성 확인
print(dir(f))
print()

# 인코딩 확인
print(f.encoding)
print()

# 파일이름
print(f.name)
print()

# 모드 확인
print(f.mode)
print()

# 파일 안의 내용물 보기
content = f.read()
print(content)
print()

# 다 사용한뒤에는 반드시 close()
f.close()



# 예제2
# 예제1 에 나왔던 것처럼 해도 되지만 다음과 같은 방법도 있다.
# 굳이 close 를 따로 해주지 않아도 되고 들여쓰기 덕분에 가독성이 좋다.
# with open('./readTest/test1.txt', 'rt', encoding='UTF-8') as f:
#     c = f.read()
#     print(c)
#     print(iter(c))
#     print(list(c))
# print()


# 예제3
# read(): 전체 읽기
# read(10): 10byte 씩 읽기

with open('./readTest/test2.txt', 'r', encoding='UTF-8') as f:
    c = f.read(10)  # 10byte 갖고 오고 끝난 지점에 cursor 를 남김
    print(c)
    c = f.read(10)  # cursor 가 남았던 지점 이후에 10byte 를 가져옴.
    print(c)
    f.seek(0,0)     # 모든 cursor 초기화. 처음 부분으로 돌아감.
    c = f.read(10)
    print(c)
print()


# 예제4
# readline: 한 줄씩 읽기
with open('./readTest/test1.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
print()


# 예제5
# readlines: 전체를 읽은 후에 라인 단위로 리스트 형태 저장
with open('./readTest/test1.txt', 'r', encoding='UTF-8') as f:
    content = f.readlines()
    print(content)
    print()
    for c in content:
        print(c, end='')
print()




# 파일쓰기(write)

# 예제1
# with open('./writeTest/content1.txt', 'w') as f:
#     f.write('Python is good :)\n')


# 예제2
with open('./writeTest/content1.txt', 'a') as f:
    f.write('Python is good :)\n')



# 예제3
# writelines: 리스트의 내용을 파일에 입력
with open('./writeTest/content1.txt', 'a') as f:
    l = ['Apple\n', 'Banana\n', 'Citra\n', 'Durian\n']
    f.writelines(l)


# 예제4
# 터미널로 출력안하고 파일에 출력하는 방법
with open('./writeTest/content1.txt', 'a') as f:
    print('Hello, python', file=f)