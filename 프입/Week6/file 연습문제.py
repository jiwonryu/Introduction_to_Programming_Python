f_in = open('proverbs.txt','r')
f_out = open('output.txt','w')
i = 1
for line in f_in:
    f_out.write(str(i)+": "+line)
    i = i + 1
f_in.close()
f_out.close()

f = open('proverbs.txt','r')
lines = f.readlines()
freq = {}
for line in lines:
    for char in line.strip():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
print(freq)
f.close()
