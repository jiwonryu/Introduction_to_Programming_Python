f = open("CSV.txt",'w')
f.write("1/2/2019,5,8,red\n1/3/2019,5,2,green\n1/4/2019,9,1,blue")
f.close()

f = open("CSV.txt",'r')
lines = f.readlines()
for line in lines:
    print(line.strip())
    parts = line.split(',')
    for part in parts:
        print(' ', part)
f.close()