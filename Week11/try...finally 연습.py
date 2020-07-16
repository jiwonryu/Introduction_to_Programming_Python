try:
    print("예외가 있을 떄")
    number = 4/0 #ZeroDivisionError 발생
    print("다음 코드들 ...")
except:
    print("except 블록")
else:
    print("else 블록")
finally:
    print("finally 블록")
print('**********')
try:
    print("예외가 없을 때")
    number = 4/4
    print('다음 코드들...')
except:
    print('except블록')
else:
    print('else블록')
finally:
    print('finally블록')