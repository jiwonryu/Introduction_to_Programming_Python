import random
import time

op = ['+','-','*']

#def random_op(data):
#    operator = random.choice(op)
#    return operator
i = 1
score = 0
while i < 6: # 문제 5번 출제 반복
    x = random.randint(10, 99) # 첫번째 임의의 두자릿수 정수 생성
    y = random.randint(10, 99) # 두번째 임의의 두자릿수 정수 생성
    operator = random.choice(op)
    start = time.time()
    your_answer = int(input('문제%d: %d%s%d?'%(i,x,operator,y))) # 문제 출제 (답 입력받음)
    end = time.time()
    if operator == '+':
        if your_answer == x+y: #입력한 답이 정답이면
            if end - start <= 10:
                print("시간내에 맞췄습니다.")
                score += 1
            else:
                print("답을 맞췄으나 시간이 초과되었습니다.")
        else: #입력한 답이 오답이면
            print("틀렸습니다!")
    elif operator == '-':
        if your_answer == x-y:
            if end - start <= 10:
                print("시간내에 맞췄습니다.")
                score += 1
            else:
                print("답을 맞췄으나 시간이 초과되었습니다.")
        else:
            print("틀렸습니다!")
    elif operator == '*':
        if your_answer == x*y:
            if end - start <= 10:
                print("시간내에 맞췄습니다.")
                score += 1
            else:
                print("답을 맞췄으나 시간이 초과되었습니다.")
        else:
            print("틀렸습니다!")
    i = i+1 # 문제 번호 추가
print('정답을 맞춘 갯수: %d/5' %score)
