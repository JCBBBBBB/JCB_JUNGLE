# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
time = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    t = data[0]         # i번 작업 시간
    cnt = data[1]       # 선행 작업 개수
    prereqs = data[2:]  # 선행 작업 번호들

    time[i] = t

    for p in prereqs:
        graph[p].append(i)   # p를 끝내야 i 가능
        indegree[i] += 1

queue = deque()

# 선행 작업 없는 애들은 바로 시작 가능
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    cur = queue.popleft()

    for nxt in graph[cur]:
        # nxt 작업의 완료 시간 갱신
        dp[nxt] = max(dp[nxt], dp[cur] + time[nxt])

        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(max(dp))