#practice
pocket = ['paper','cellphone','notebook']
card = 1
if 'money' in pocket:
    print("돈이 있으니 택시를 타고 가라")
else:
    if card:
        print("카드가 있으니 택시를 타고 가라")
    else:
        print("걸어가라")

#홀/짝
print("====짝/홀수 판별 프로그램====")
N = int(input("수를 입력하세요: "))
print("%d을(를) 입력하셨습니다." %N)
if N> 0:
    if N % 2 == 0:
        print("%d은(는) 짝수입니다." %N)
    else:
        print("%d은(는) 홀수입니다." %N)
else:
    print("판별할 수 없는 수를 입력하였습니다.")