#2-1
class PythonLecture:
    def __init__(self,first,second,third,absence): # __init__함수
        self.first = float(first) # 1차 시험 점수
        self.second = float(second) # 2차 시험 점수
        self.third = float(third) # 3차 시험 점수
        self.absence = float(absence) # 결석 횟수
        # 뒤에서 계산 원활히 하기 위해 자료형은 '실수형'으로 맞춰줌

    def average(self): # 3개의 시험의 평균 점수를 산출하는 함수
        avg = (self.first+self.second+self.third)/3 # 세 점수의 평균
        return "{0:0.2f}".format(avg) # 소수점 두자리까지 반환

    def score(self): # 3개의 점수를 20%, 30%, 50% 가중치로 평균을 산출하는 함수
        result =  (self.first*0.2)+(self.second*0.3)+(self.third*0.5)
        return "{0:0.2f}".format(result) # 소수점 두자리까지 반환
#2-2
    def grade(self): # 학점을 산출하는 함수
        score = float(PythonLecture.score(self)) # 위에서 정의한 score 함수의 반환값
        if self.absence >= 5: # 결석이 5회 이상일 때
            return ("F")
        else: # 결석이 5회 미만일 때
            if score >= 90 and score <= 100: # 90점 이상~100점
                return("A")
            elif score >= 80 and score < 90: # 80점 이상~90점 미만
                return("B")
            elif score >= 70 and score < 80: # 70점 이상~80점 미만
                return("C")
            elif score >= 60 and score < 70: # 60점 이상~70점 미만
                return("D")
            elif score < 60: # 60점 미만
                return("F")