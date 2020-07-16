#practice1 while예제
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍엇습니다." %treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

#pracitce2 while+if 예제
prompt = """
1.Add
2.Del
3.List
4.Quit
Enter number: """

print(prompt)
number = int(input())

while number:
    if number !=4:
        print(prompt)
        number = int(input())
    elif number == 4:
        print("종료!")
        break

#practice3 while문 강제로 빠져나가기
coffee = 3
while True : #커피와 돈이 모두 있는 동안
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    el


