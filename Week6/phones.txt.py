f = open("phones.txt",'w')
f.write("""눈송이 010-1234-5678
꽃송이 010-1234-5679
별송이 010-1234-5680""")
f.close()

#readline()
f = open("phones.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line.rstrip())
f.close()

#readlines()
f = open("phones.txt",'r')
lines = f.readlines()
for line in lines:
    print(line.rstrip())
f.close()

#read()
f = open("phones.txt",'r')
data = f.read()
print(data)
f.close()

f = open("phones.txt",'a')
f.write("\n꿀송이 010-1234-4581")
f.close()