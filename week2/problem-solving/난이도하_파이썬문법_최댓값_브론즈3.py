# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562






import sys
input = sys.stdin.readline



num_list = []
#원본 보관
copy_list = []

for i in range(9):
    num = int(input())
    num_list.append(num)

copy_list = num_list.copy()

for i in range(8):
    temp = num_list[i]
    for j in range(i+1, 9):
        if(temp >= num_list[j]):
            temp = num_list[j]
    
    for k in range(i+1, 9):
        if(temp == num_list[k]):
            num_list[i], num_list[k] = num_list[k], num_list[i]



for i in range(9):
    #원본 값중에 최대값이랑 같으면 그게 최댓값이 몇번째 수 인지 알 수있다
    if(copy_list[i] == num_list[8]):
        num = i
        break


print(num_list[8])
print(num+1)
