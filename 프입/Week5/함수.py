#1-1
def is_even(n):
    if n%2 == 0:
        print("True")
    else:
        print("False")
a = int(input("정수를 입력하세요:"))
is_even(a)

#1-2
def get_avg(*args):
    sum = 0
    for i in args:
        sum = sum + i
        avg =  sum / len(args)
    return avg

print(get_avg(1,3,5,7,9))