# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

from collections import deque


num = int(input())

pair_num = int(input())


graph = {}
visited = []
answer = 0

for i in range(pair_num):
    a,b = map(int, input().split())

    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

queue = deque()

queue.append(1)
visited.append(1)

while(queue):
    cur = queue.popleft() #graph = {}

    if cur in graph: # ex-> 1이 그래프 키에 있냐
        for next in graph[cur]:
            if(next not in visited):
                answer += 1
                queue.append(next)
                visited.append(next)


print(answer)


# //  graph = {
#         0: [1, 2],
#         1: [0, 2],
#         2: [0, 1, 3],
#         3: [2]
#     }
