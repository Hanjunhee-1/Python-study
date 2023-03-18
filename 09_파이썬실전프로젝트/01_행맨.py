# Hangman(행맨) 미니 게임 제작

import time
import csv
import random
import winsound

name = input('What\'s your name?: ')

print('Hi, ' + name, 'Time to play Hangman game!!!')

print()

time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# csv 단어 예시
words = []

with open('./examples.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    
    # header skip
    next(reader)

    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)

# 랜덤하게 선택
q = random.choice(words)

# 정답 단어
word = q[0].strip()


# 사용자 추측 단어
guesses = ''

# 기회
chance = 10

print('Hint: ' + q[1])

while chance > 0:

    # 실패횟수
    failed = 0

    # 정답 단어 반복

    for char in word:

        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어를 출력
            print(char, end=' ')
        else:
            # 틀린 경우 '_' 로 처리
            print('_', end=' ')
            failed+=1

    # 단어 추측을 성공한 경우
    if failed == 0:
        print()
        print()

        # 성공했을 경우 소리 출력
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations! You win!')
        break
    print()

    # 추측 단어 문자 단위 입력받기
    print()
    guess = input('guess a character: ')

    guesses += guess


    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        chance -= 1
        # 오류 메시지
        print('Wrong X(')

        # 남은 기회 출력
        print('You have', + chance, 'more guesses!')

        if chance == 0:
            # 실패했을 경우 소리 출력
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            # 실패 메시지
            print('You lose')