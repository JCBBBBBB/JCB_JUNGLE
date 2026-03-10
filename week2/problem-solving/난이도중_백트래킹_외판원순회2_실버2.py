# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

import sys
n = int(input())

w = [list(map(int,input().split())) for _ in range(n)]
sums = [sys.maxsize]

def backtracking(start, visited):
    if (len(visited) == n):
        visited.append(visited[0])
        sum = 0
        for i in range(len(visited) -1):
            if (w[visited[i]][visited[i+1]] == 0):
                visited.pop()
                return
            sum += w[visited[i]][visited[i+1]]
        if sums[0] > sum:
            sums[0] = sum
        visited.pop()
        return
    
    for i in range(1, n):
        if i not in visited:
            visited.append(i)
            backtracking(visited[len(visited) -1], visited)
            visited.pop()

backtracking(0, [0])

print(sums[0])