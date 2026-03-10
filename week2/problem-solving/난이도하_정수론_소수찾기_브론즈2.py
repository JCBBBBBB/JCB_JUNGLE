# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

num = int(input())

data = list(map(int, input().split()))

answer = 0

for i in range(num):
    temp_list =[]
    for j in range(1, data[i] + 1):
        if(data[i] % j == 0):
            temp_list.append(j)

    if(len(temp_list) == 2):
        answer += 1

print(answer)