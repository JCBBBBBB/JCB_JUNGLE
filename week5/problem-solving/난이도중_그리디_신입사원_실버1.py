# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

T = int(input())


for i in range(T):
    N = int(input())

    rank_list = list()
    answer = 1
    for j in range(N):
        first_rank, second_rank = map(int, input().split())
        rank_list.append((first_rank, second_rank))

    rank_list.sort()

    standard_num = rank_list[0][1]
    for k in range(1, len(rank_list)):
        if(rank_list[k][1] < standard_num): #다음게 더 작으면
            answer += 1
            standard_num = rank_list[k][1]
    print(answer)

