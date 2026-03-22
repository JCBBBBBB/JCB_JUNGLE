# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import deque

def dfs(start):
    stack = []
    visited = []
    stack.append(start)
    visited.append(start)

    while(stack):
        cur = stack.pop()
        if(cur not in visited):
            visited.append(cur)

        for next in reversed(graph[cur]):
            if(next not in visited):
                stack.append(next)

    for inside in visited:
        print(inside, end =' ')


def bfs(start):
    queue = deque()
    visited = []
    queue.append(start)
    visited.append(start)

    while(queue):
        cur = queue.popleft()

        for next in graph[cur]:
            if(next not in visited):
                queue.append(next)
                visited.append(next)

    for inside in visited:
        print(inside, end =' ')





if __name__ == "__main__":
    N, M, V = map(int, input().split())

    graph = {i: [] for i in range(1, N+1)}

    for i in range(M):
        x,y = map(int, input().split())
        graph.setdefault(x, []).append(y)
        graph.setdefault(y, []).append(x)

    for key in graph:
        graph[key].sort() 

    dfs(V)
    print()
    bfs(V)