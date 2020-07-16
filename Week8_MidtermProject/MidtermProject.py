#1 자기소개 txt 작성
#1-1)
f = open("1816506_류지원.txt",'w')
f.write('〓'*30)
f.write('\n프로그래밍 입문 중간고사 답안지\n')
f.write('〓'*30)
f.write('\n학번: 1816506\n이름: 류지원\n')
f.write('▽▼'*15)
#1-2)
f.write('\nSookmyung Women\'s University')
f.close()

#1-3)
with open("1816506_류지원.txt",'a') as f:
    data = """
▶ 학과: 전자공학전공 (복수전공: 미디어학부)
▶ 고향: 경상남도 김해시
▶ 나이: 22살
♥ 취미: 독서, 글쓰기, 영화 감상, 요가
♥ 좋아하는 음식: 떡볶이
♥ 좋아하는 장소: 한강
♥ 좋아하는 영화: 라라랜드"""
    f.write(data)

#1-4)
print("\n# 1번 문제: 자기소개 답안지 txt\n")
with open("1816506_류지원.txt",'r') as f:
    readData = f.read()
    print(readData)

#2 커피 자판기
print("\n\n# 2번 문제: 커피 자판기\n")
#2-1)
class Twosome:
    def __init__(self,price,cal,rest):
        self.__price = price
        self.__cal = cal
        self.__rest = rest
#2-2)
    def getRest(self):
        if (self.__rest) == 0:
            print("죄송하지만 선택하신 음료의 잔여 수량이 0입니다.\n선택하신 음료를 판매할 수 없습니다.\n")
        else:
            self.__rest = self.__rest
        while self.__rest: #잔여 수량이 있는 동안
            self.__rest = self.__rest - 1
            break


#2-3)
    def getBeverage(self):
        return "%d원/%dKcal/잔여수량:%d" %(self.__price,self.__cal,self.__rest)
#2-4)
Americano = Twosome(4100,15,10)
Latte = Twosome(4600,100,3)
Mocha = Twosome(5100,270,5)

#2-5)
print("챗봇> 반갑습니다. 여기는 Twosome 입니다.")
menu = 1
while menu:
    print('〓'*32)
    print("{0:*^41}".format(" Twosome 메뉴판 "))
    print("1. 아메리카노", Americano.getBeverage())
    print("2. 카페 라떼", Latte.getBeverage())
    print("3. 카페 모카",  Mocha.getBeverage())
    print("4. 나가기")
    print('〓'*32)
    beverage = int(input("챗봇> 원하시는 메뉴를 선택해주세요: "))
    if beverage == 1:
        print("아메리카노를 주문하셨습니다.")
        Americano.getRest()
        a = int(input("음료를 더 주문하시려면 1, 종료하시러면 2를 눌러주세요: "))
        if a == 1: menu = True
        elif a == 2: menu = False

    elif beverage == 2:
        print("카페 라떼를 주문하셨습니다.")
        Latte.getRest()
        b = int(input("음료를 더 주문하시려면 1, 종료하시러면 2를 눌러주세요: "))
        if b == 1: menu = True
        elif b == 2: menu = False

    elif beverage == 3:
        print("카페 모카를 주문하셨습니다.")
        Mocha.getRest()
        c = int(input("음료를 더 주문하시려면 1, 종료하시러면 2를 눌러주세요: "))
        if c == 1: menu = True
        elif c == 2: menu = False

    elif beverage == 4:
        break
    else :
        print("없는 메뉴입니다. 다른 메뉴를 선택해주세요.")

print("이용해주셔서 감사합니다. 안녕히 가세요.")



