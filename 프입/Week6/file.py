f = open("새파일.txt",'w')
for i in range(1,11):
    data = "%d번 째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("새파일.txt", 'a')
for i in range(11,20):
    data = "%d번 째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()