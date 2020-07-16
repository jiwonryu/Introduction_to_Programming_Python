n = int(input('몇 단을 출력할까요?: '))
import time
def GuGu(n):
    for i in range(1,10):
        print(str(n), 'X', str(i), '=', str(n*i) )
        time.sleep(1)
GuGu(n)
