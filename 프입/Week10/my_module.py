# my_module.py
PI = 3.14

class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        area = PI*(self.r**2)
        print('반지름이 ', self.r, '인 원의 넓이는 ', area)

class Square:
    def __init__(self, l):
        self.l = l
    def area(self):
        area = self.l**2
        print('한 변의 길이가 ', self.l, '인 정사각형의 넓이는 ', area)

        