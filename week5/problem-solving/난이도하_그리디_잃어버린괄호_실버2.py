# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541


import re
import this



# 55-50+40    #-50-50-50    #10+20+30+40    #00009-00009
sentence = str(input())

# 55, 50+40   '' 50 50 50         10+20+30+40        00009   00009
sentence = sentence.split('-')

answer = 0
for i in range(len(sentence)):
    if(sentence[i] == ''):
        continue
    
    # 50+40
    temp = sentence[i].split('+')

    for j in range(len(temp)): #문자열로 저장된 sentence를 정수로 바꿔준다
        temp[j] = int(temp[j])


    if(i == 0):
        answer += sum(temp)
    else:
        answer -= sum(temp)

print(answer)