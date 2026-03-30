# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys
from collections import deque


def solution(N, visited, small_stone_list):

    queue = deque([(1,0,0)])

    while(queue):
        location, jump, n = queue.popleft()

        for x in [jump-1, jump, jump + 1]:
            if x > 0:
                next_location = location + x
                if next_location == N:
                    return n + 1
                if next_location < N and next_location not in small_stone_list and x not in visited[next_location]:
                    visited[next_location].append(x)
                    queue.append((next_location, x, n+1))
        return -1

if __name__ == "__main__":

    N, M = map(int, input().split())
    visited = [[] for _ in range(N+1)]
    small_stone_list = set()

    for i in range(M):
        small_stone = int(input())
        small_stone_list.add(small_stone)
    print(solution(N, visited, small_stone_list))

#jump_num을 