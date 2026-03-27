# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047


N, K = map(int, input().split())

coin_list = list()

for i in range(N):
    price = int(input())
    coin_list.append(price)

answer = 0

for i in range(N-1, -1, -1):
    if(K == 0):
        break
    share = K // coin_list[i]

    if(share !=0):
        answer += share

    K = K % coin_list[i]

print(answer)