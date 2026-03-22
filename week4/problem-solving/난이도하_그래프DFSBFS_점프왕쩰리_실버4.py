# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173


from collections import deque
import sys


def function():
    N = int(input())

    arr = []

    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    queue = deque()

    visited = [[False] * (N+1) for _ in range(N+1)]
    queue.append((1,1))
    visited[1][1] = True

    while(queue):
        x,y = queue.popleft() #큐의 처음 값 가져온다

        #1,1 부터 시작한다 치면
        
        #지금 현재 x,y에 있는 area값을 더해주면 그 방향 if로 해서 넘으면 continue
        area_num = int(arr[x-1][y-1])

        if(area_num == -1):
            print('HaruHaru')
            return

        if((x + area_num >= 1 and x + area_num <= N) and (y >= 1 and y <= N)):
            if(visited[x + area_num][y] == False):
                queue.append((x+area_num, y))
                visited[x+area_num][y] = True
        
        if((x>= 1 and x <= N) and (y + area_num >= 1 and y + area_num <= N)):
            if(visited[x][y + area_num] == False):
                queue.append((x, y + area_num))
                visited[x][y+area_num] = True

    print('Hing')
        #다 넘기면 queue에 넣는다

if __name__ == "__main__":
    function()