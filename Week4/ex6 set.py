A = set(['Lee','Sanders','Harris','Davis'])
B = set(['Park','Harris','Clark','Lee'])

print("2개의 파티에 모두 참석한 사람은 다음과 같다")
nameList = list(A&B)
nameList.sort()

print(nameList)
