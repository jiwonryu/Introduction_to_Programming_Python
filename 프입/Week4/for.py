#1 forMarks.py
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number+1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." %number)

#2 for+range
marks = [90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60: continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))

#3 구구단
for i in range(2,10):
    print("구구단 %d단 시작! "%i, end="")
    for j in range(1,10):
        print(i*j, end=" ")
    print("")

#3 구구단 리스트에 포함
result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)

#연습문제 1
A = [70,60,55,75,95,90,80,85,100]
sum = 0
for number in range(len(A)):
    sum += A[number]
avg = sum / len(A)
above = [score for score in A if score>=avg]
print("Average is", avg)
print("Scores above average are", above)

