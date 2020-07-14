print("1부터 100사이의 숫자를 맞추시오.")
import random
number = random.randint(1,100)
i = 0
print("정답=", number)
while True:
    N = int(input("숫자를 입력하세요:"))
    i += 1
    if N < number:
        print("낮음! 시도횟수 = ", i)
    elif N > number:
        print("높음! 시도횟수 =", i)
    else:
        break
print("축하합니다. 시도횟수 = ", i)