#2-3
from mod_scoregrade import PythonLecture
#앞에서 만든 모듈의 PythonLecture Class 불러옴

print("="*30)
print("Python Lecture Score Calculator")
print("="*30)

fst1, sec1, thrd1, absnc1 = input("Student 1 > ").split()
fst2, sec2, thrd2, absnc2 = input("Student 2 > ").split()
fst3, sec3, thrd3, absnc3 = input("Student 3 > ").split()
# 3명의 학생의 1차, 2차, 3차 시험 점수와 결석 횟수 입력 받음

std1 = PythonLecture(fst1, sec1, thrd1, absnc1)
std2 = PythonLecture(fst2, sec2, thrd2, absnc2)
std3 = PythonLecture(fst3, sec3, thrd3, absnc3)
# 입력받은 시험 점수와 결석 횟수를 PythonLecture Class에 대입한 인스턴스 3개 생성

print("{0:=^30}".format(" Result "))
print("Num  Score  Grade")

print("{0:^3}".format('1'), "{0:^7}".format(std1.score()), "{0:^5}".format(std1.grade()))
print("{0:^3}".format('2'), "{0:^7}".format(std2.score()), "{0:^5}".format(std2.grade()))
print("{0:^3}".format('3'), "{0:^7}".format(std3.score()), "{0:^5}".format(std3.grade()))
# 학생 번호, 점수, 학점 반환 (가운데 정렬하여 깔끔하게 출력)