#1-1
import random # 난수 발생 위한 모듈

i = 1
while i < 6: # 문제 5번 출제 반복
    x = random.randint(10, 99) # 첫번째 임의의 두자릿수 정수 생성
    y = random.randint(10, 99) # 두번째 임의의 두자릿수 정수 생성
    your_answer = int(input('문제 %d: %d+%d?'%(i,x,y))) # 문제 출제 (답 입력받음)
    if your_answer == x+y: #입력한 답이 정답이면
        print("정답입니다!")
    else: #입력한 답이 오답이면
        print("틀렸습니다!")
    i = i+1 # 문제 번호 추가


#1-2
import random # 난수 발생 위한 모듈

op = ['+','-','*'] # 연산자 리스트

i = 1 # i 정의 (문제 번호, 초기 = 1)
while i < 6: # 문제 5번 출제 반복
    x = random.randint(10, 99) # 첫번째 임의의 두자릿수 정수 생성
    y = random.randint(10, 99) # 두번째 임의의 두자릿수 정수 생성
    operator = random.choice(op) # 랜덤으로 반환된 연산자
    your_answer = int(input('문제%d: %d%s%d?'%(i,x,operator,y))) # 문제 출제 (답 입력받음)
    if operator == '+': # 연산자가 + 일때
        if your_answer == x+y: # 입력한 답이 정답이면
            print("정답입니다!")
        else: # 입력한 답이 오답이면
            print("틀렸습니다!")
    elif operator == '-': # 연산자가 - 일때
        if your_answer == x-y:
            print("정답입니다!") # 입력한 답이 정답이면
        else: # 입력한 답이 오답이면
            print("틀렸습니다!")
    elif operator == '*': # 연산자가 * 일때
        if your_answer == x*y:
            print("정답입니다!") # 입력한 답이 정답이면
        else: # 입력한 답이 오답이면
            print("틀렸습니다!")
    i = i+1 # 문제 번호 추가

#1-3

import random # 난수 발생 위한 모듈
import time # 시간 관련 모듈

op = ['+','-','*']

i = 1
score = 0
while i < 6: # 문제 5번 출제 반복
    x = random.randint(10, 99) # 첫번째 임의의 두자릿수 정수 생성
    y = random.randint(10, 99) # 두번째 임의의 두자릿수 정수 생성
    operator = random.choice(op)
    start = time.time() # 문제 출제 직전 시간
    your_answer = int(input('문제%d: %d%s%d?'%(i,x,operator,y))) # 문제 출제 (답 입력받음)
    end = time.time() # 답 입력 직후 시간
    if operator == '+': # 연산자가 + 일때
        if your_answer == x+y: # 입력한 답이 정답이면
            if end-start <= 5: # 경과시간이 5초 이하일 때
                print("시간내에 맞췄습니다.")
                score += 1 # 점수 1점 증가
            else: # 경과시간이 5초를 초과했을 때
                print("답을 맞췄으나 시간이 초과되었습니다.")
        else: # 입력한 답이 오답이면
            print("틀렸습니다!")
    elif operator == '-': # 연산자가 - 일때
        if your_answer == x-y: # 입력한 답이 정답이면
            if end-start <= 5: # 경과시간이 5초 이하일 때
                print("시간내에 맞췄습니다.")
                score += 1 # 점수 1점 증가
            else: # 경과시간이 5초를 초과했을 때
                print("답을 맞췄으나 시간이 초과되었습니다.")
        else: # 입력한 답이 오답이면
            print("틀렸습니다!")
    elif operator == '*': # 연산자가 * 일때
        if your_answer == x*y: # 입력한 답이 정답이면
            if end-start <= 5: # 경과시간이 5초 이하일 때
                print("시간내에 맞췄습니다.")
                score += 1 # 점수 1점 증가
            else: # 경과시간이 5초를 초과했을 때
                print("답을 맞췄으나 시간이 초과되었습니다.")
        else: # 입력한 답이 오답이면
            print("틀렸습니다!")
    i = i+1 # 문제 번호 추가
print('정답을 맞춘 갯수: %d/5' %score) # 정답을 맞춘 갯수 출력