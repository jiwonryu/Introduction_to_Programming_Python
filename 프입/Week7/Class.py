class Service:
    secret = '영구는 배꼽이 두개다.'
    def __init__(self, name):
        self.name = name
    def sum(self,a,b):
        result = a+b
        print("%s님, %s + %s = %s입니다."%(self.name,a,b,result))
pey = Service('홍길동')
pey.sum(1,1)

class FourCal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        result = self.a + self.b
        return result
    def mul(self):
        result = self.a * self.b
        return result
    def sub(self):
        result = self.a - self.b
        return result
    def div(self):
        result = self.a - self.b
        return result
Cal1 = FourCal(4,2)
print(Cal1.sum())