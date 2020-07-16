# ex1.py
class BankAccount:
    def __init__(self, name='None', balance=0):
        self.name = name
        self.balance = balance
        print(self.name, "님 환영합니다.")
        print("초기 금액", self.balance, "으로 계좌가 만들어졌습니다.")

    def deposit(self, amount):
        self.balance += amount
        print("통장에 ", amount, "가 입금 되었음")
        print("현재 잔액은", self.balance, "입니다.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("통장에 ", amount, "가 출금되었음")
        else:
            print("출금하려는 금액이 현재 잔액보다 큽니다.")
            print("출금이 이루어지지 않습니다.")
        print("현재 잔액은 ", self.balance, "입니다.")

a = BankAccount('지원')
a.deposit(100)
a.withdraw(200)
a.withdraw(50)