# practice 1
import time

def fib(n):
    a,b = 0,1
    while b<n:
        print(b, end='')
        a, b = b, a+b
        time.sleep(0.1)


start = time.time()
fib(1000)
end = time.time()
print('\nElapsed time (sec): %.10f' % (end-start))