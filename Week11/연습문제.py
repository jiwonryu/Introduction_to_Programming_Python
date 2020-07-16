#1
while True:
    try:
        n = int(input('숫자를 입력하세요:' ))
        break
    except ValueError:
        print('정수가 아닙니다. 다시 입력하시오.')
print('정수 입력이 성공하였습니다!')

#2
while True:
    bread = 10
    try:
        n = int(input('몇 명?'))
        print('1인당 빵의 수: ', bread/n)
        break
    except ValueError:
        print('입력이 잘못되었습니다.')
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
print('맛있게 드세요.')