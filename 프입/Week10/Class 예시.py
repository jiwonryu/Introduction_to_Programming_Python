#1 연산자 오버로딩 예시1
class A:
    def __init__(self, a):
        self.a = a
    def ___add__(self,o):
        return self.a + o.a

ob1 = A(1)
ob2 = A(2)
print(ob1+ob2)
ob3 = A('Hi')
ob4 = A('Python')
print(ob3 + ob4)
print(ob1 + ob3)

#3 연산자 오버로딩 예시3
class B:
    def __init__(self,a):
        self.a = a
    def __gt__(self,other):
        if self.a > other.a:
            return True
        else:
            return False

ob1 = B(1)
ob2 = B(2)
print(ob1 > ob2)
print(ob1 < ob2)

if ob > ob2:
    print('ob1 is greater than ob2')
else:
    print('ob2 is greater than ob1')

