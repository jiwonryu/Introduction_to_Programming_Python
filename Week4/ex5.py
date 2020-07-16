engDict = dict()
engDict['one']='하나'
engDict['two']='둘'
engDict['three']='셋'

word = input("단어를 입력하세요: ")
print(engDict.get(word, '없음'))
