# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque

N = int(input())
K = int(input())

board = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 'Apple'

L = int(input())
turns = {}

for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

# 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0
time = 0

snake = deque()
snake.append((1, 1))
board[1][1] = 'Snake'

while True:
    time += 1

    head_x, head_y = snake[-1]
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    # 벽 충돌
    if nx < 1 or nx > N or ny < 1 or ny > N:
        print(time)
        break

    # 몸 충돌
    if board[nx][ny] == 2:
        print(time)
        break

    # 사과가 있으면 꼬리 유지
    if board[nx][ny] == 'Apple':
        board[nx][ny] = 'Snake'
        snake.append((nx, ny))
    else:
        board[nx][ny] = 'Snake'
        snake.append((nx, ny))
        tx, ty = snake.popleft()
        board[tx][ty] = 0

    # 방향 전환
    if time in turns:
        if turns[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
