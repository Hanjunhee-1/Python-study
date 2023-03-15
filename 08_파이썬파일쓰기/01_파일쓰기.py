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