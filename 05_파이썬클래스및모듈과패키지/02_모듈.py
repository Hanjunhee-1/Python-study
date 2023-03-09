# module: 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

# 해당 실습 내용은 ../module_test 폴더와 같이 볼것!

# sys 모듈 import
import sys

# python 경로 확인
# print(sys.path)


# 자신이 만든 모듈 경로 추가
sys.path.append('C:/Users/wnswn/Desktop/인프런_스터디모음/python공부/module_test')


# 추가되었는지 확인
# print(sys.path)


# vscode 에서는 settings.json 을 수정해야하는데 '빠른 수정' 으로 해결가능

# 모듈 import 해서 사용해보기
import my_module
print(my_module.power(10, 2))  # 이렇게 사용하고 나면 '__pycache__' 라는 폴더가 생김
