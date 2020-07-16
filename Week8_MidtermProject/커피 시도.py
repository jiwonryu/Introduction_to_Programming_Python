# 2 커피 자판기
print("\n\n# 2번 문제: 커피 자판기\n")


# 2-1)
class Twosome:
    def __init__(self, price, cal, rest):
        self.__price = price
        self.__cal = cal
        self.__rest = rest

# 2-2)
    def getRest(self):
        if (self.__rest) == 0:
            print("죄송하지만 선택하신 음료의 잔여 수량이 0입니다.\n선택하신 음료를 판매할 수 없습니다.")
        else:
            self.__rest = self.__rest
        while self.__rest:  # 잔여 수량이 있는 동안
            self.__rest = self.__rest - 1
            break

# 2-3)
    def getBeverage(self):
        return "%d원/%dKcal/잔여수량:%d" % (self.__price, self.__cal, self.__rest)
# 2-4)
Americano = Twosome(4100, 15, 10)
Latte = Twosome(4600, 100, 3)
Mocha = Twosome(5100, 270, 5)

def choiceOrder():
    choice = 1
    while choice:
        a = int(input("음료를 더 주문하시려면 1, 종료하시러면 2를 눌러주세요: "))
        if a == 1:
            choice = False
        elif a == 2:
            choice = False
        else:
            print("다시 선택해주세요.")
            choice = True

            # 2-5)
print("챗봇> 반갑습니다. 여기는 Twosome 입니다.")
get_menu = 1
while get_menu:
    print('〓' * 32)
    print("{0:*^41}".format(" Twosome 메뉴판 "))
    print("1. 아메리카노", Americano.getBeverage())
    print("2. 카페 라떼", Latte.getBeverage())
    print("3. 카페 모카", Mocha.getBeverage())
    print("4. 나가기")
    print('〓' * 32)
    beverage = int(input("챗봇> 원하시는 메뉴를 선택해주세요: "))
    if beverage == 1:
        print("아메리카노를 주문하셨습니다.")
        Americano.getRest()
        choiceOrder()

    elif beverage == 2:
        print("카페 라떼를 주문하셨습니다.")
        Latte.getRest()
        choiceOrder()

    elif beverage == 3:
        print("카페 모카를 주문하셨습니다.")
        Mocha.getRest()
        choiceOrder()

    elif beverage == 4:
        break
    else:
        print("없는 메뉴입니다. 다른 메뉴를 선택해주세요.")


print("이용해주셔서 감사합니다. 또 뵙겠습니다.")
