# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541


import re
import this

example = str(input())

example = example.split('-')
# 55  -   50+40   -   30+20

#55   50\
temp_sum = 0
for i in range(len(example)):
    if(example[i] == ''):
        continue
    temp = example[i].split('+')
    for j in range(len(temp)): #int 변환
        temp[j] = int(temp[j])

    if i==0:
        temp_sum += sum(temp)
    else:
        temp_sum -= sum(temp)   # 90   50


print(temp_sum)

