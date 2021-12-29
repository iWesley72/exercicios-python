from typing import List


l = []
for i in range(0, 5):
    num = int(input('Digite algum número: '))
    l.append(num)
print('O maior número é', max(l, key=int))