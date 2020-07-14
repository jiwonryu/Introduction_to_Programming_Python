#practice 2

import random
import statistics as

scores = []
for i in range(10):
    scores.append(random.randint(1,100))

print('='*23)
print('Gradebook of This Class')
print('='*23)
print('scores: ', end='')
for i in range(len(scores)):
    print(scores[i], end=' ')

print()
print('Average score: %.2f' %stat.mean(scores))
print('Highest score: %d' %max(scores))
print('Lowest score: %d' %min(scores))
print('Median score: %d' %stat.median(scores))