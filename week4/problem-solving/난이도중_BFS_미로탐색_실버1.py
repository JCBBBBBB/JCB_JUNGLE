# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

#처음에 그냥 NxN 인줄 알고 했다가 계속 오류남 NxM이다

from collections import deque

N,M = map(int, input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

#배열에 갈수 있는 곳을 1로 갈수 없는 곳을 0으로
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = [[0]*M for _ in range(N)]
#(1,1)부터 출발하여 (N,M) 위치로 이동할 때 지나야 하는 최소의 칸 수
queue = deque()

#visited 필요한 이유 : 그냥 arr로 하면 내가 간 위치를 표시할 수 없다
queue.append((0,0))
visited[0][0] = True
answer[0][0] = 1

while(queue):
    x,y = queue.popleft() #현재 내가 있는 위치

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 방문한 적 없고, 갈 수 있는 길이면 queue에 넣고
        if(nx < 0 or nx >= N or ny < 0 or ny >= M):
            continue
        if(visited[nx][ny]): #방문한 적이 있으면
            continue
        if(arr[nx][ny] == 0): #갈수 없는 곳이면
            continue

        queue.append((nx,ny))
        visited[nx][ny] = 1
        answer[nx][ny] = answer[x][y] + 1
# 칸수 ++을 어디서 해줘야 되지?

print(answer[N-1][M-1])
