# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

from collections import deque


def bfs(start):

    
    queue.append(start)
    visited.append(start)

    while(queue):
        cur = queue.popleft()

        for next in graph[cur]:
            if(next not in visited):
                queue.append(next)
                visited.append(next)




if __name__ == "__main__":
    N, M = list(map(int, input().split()))

    graph = {i: [] for i in range(1, N+1)}


    for i in range(M):
        u, v = map(int, input().split())

        graph.setdefault(u, []).append(v) # 경로 양방향 추가
        graph.setdefault(v, []).append(u) # 경로 양방향 추가



    queue = deque()
    visited = []
    count = 0

    for i in range(1, N+1):
        if(i not in visited):
            bfs(i)
            count += 1

    print(count)