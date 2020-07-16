def get_sorted():
    a = int(input("첫 번째 정수:"))
    b = int(input("두 번째 정수:"))
    if b<a:
        return (b,a)
    else:
        return (a,b)

print(get_sorted())

print((lambda a, b: (a,b) if a<b else(b,a))(20,10))




