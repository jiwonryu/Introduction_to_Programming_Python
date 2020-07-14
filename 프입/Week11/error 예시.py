#1 에러 회피하기
try:
    f = open('없는파일','r')
except FileNotFoundError:
    pass

#2 에러 발생시키기(raise)
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print('very fast')

eagle = Eagle()
eagle.fly()

#3 직접 예외 만들기
class MyError(Exception):
    def __str__(self):
        return 'This is my error'
try:
    raise MyError
except Exception as e:
    print(e)