# csv 파일 쓰는 방법

# csv 의 mime 타입: text/csv 

import csv

# 예제1
with open('./csvTest/dummy1.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    next(reader)    # 헤더를 skip 한다. 현재 dummy.csv 에서는 name,code 부분을 skip 하게 된다.

    # 객체확인
    print(reader)

    # 타입확인
    print(type(reader))

    # 속성확인
    print(dir(reader))  # __iter__ 가 존재함. for 문에서 사용가능
    print()

    for c in reader:
        print(c)    # list 형태로 갖고옴
    print()


# 예제2
with open('./csvTest/dummy2.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f, delimiter='|')   # 기본적으로는 콤마를 기준으로 하지만 구분자 옵션을 변경해줄 수 있다.
    next(reader)    # 헤더를 skip 한다. 현재 dummy.csv 에서는 name,code 부분을 skip 하게 된다.

    for c in reader:
        print(c)
    print()


# 예제3
with open('./csvTest/dummy1.csv', 'r', encoding='UTF-8') as f:
    reader = csv.DictReader(f)  # dictionary 형태로 가져옴

    # 객체확인
    print(reader)

    # 타입확인
    print(type(reader))

    # 속성확인
    print(dir(reader))  # __iter__ 가 역시 존재.
    print()

    for c in reader:
        print(c)
        for key, value in c.items():
            print(key, value)
        print('-'*50)
    print()


# 예제4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

with open('./csvTest/writeDummy.csv', 'w', encoding='UTF-8') as f:
    c = csv.writer(f) 

    for i in w:
        c.writerow(i)   # 1,2,3 이 하나의 행으로 작성됨.



# 예제5
with open('./csvTest/writeDummy.csv', 'w', encoding='UTF-8') as f:
    fields = ['One', 'Two', 'Three']

    c = csv.DictWriter(f, fieldnames=fields)

    c.writeheader()

    for i in w:
        c.writerow({'One': i[0], 'Two': i[1], 'Three': i[2]})   # 반드시 Key 값이 따로 지정해주었던 field 의 값들과 일치해야함.