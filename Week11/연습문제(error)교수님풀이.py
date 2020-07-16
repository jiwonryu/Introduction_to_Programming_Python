class AccountException(Exception):
    pass
class AccountBalanceException(AccountException):
    def __str__(self):
        return 'Account Balance Exception Occurs: Check your balance'
class InvaildTransactionException(AccountException):
    def __str__(self):
        return 'Invalid Transaction Exception Occurs: Check your amount'

class BankAccount:
    def __init__(self, name='None', balance=0):
        self.name = name
        self.balance = balance
        print(self.name, "님 환영합니다.")
        print("초기 금액", self.balance, "으로 계좌가 만들어졌습니다.")

    def deposit(self, amount):
        try:
            if amount < 0 :
                raise InvaildTransactionException
            else:
                self.balance += amount
                print("통장에 ", amount, "가 입금 되었음")
        except InvaildTransactionException as e:
                print(e)
        finally:
            print("현재 잔액은", self.balance, "입니다.")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise AccountBalanceException
            else:
                self.balance -= amount
                print("통장에 ", amount, "가 출금되었음")
        except AccountBalanceException as e:
            print(e)
        finally:
            print("현재 잔액은 ", self.balance, "입니다.")

a = BankAccount('지원',100)
a.deposit(-100)
a.withdraw(200)
