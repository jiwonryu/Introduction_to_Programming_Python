#1
age = int(input("나이를 입력하세요: "))
height = int(input("키를 입력하세요: "))
if age >= 10 & height >= 165:
        print("놀이기구를 탈 수 있습니다.")
else:
    print("놀이기구를 탈 수 없습니다.")

#2
idList = ['Kim','Lee','Park']
id = input("아이디: ")

if id in idList:
    password = input("비밀번호: ")
    if password == '1234':
        print("환영합니다.")
    else:
        print("잘못된 패스워드입니다.")
else:
    print("알 수 없는 사용자입니다.")
