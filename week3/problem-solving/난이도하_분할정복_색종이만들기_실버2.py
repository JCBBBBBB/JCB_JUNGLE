# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

'''
solve(x, y, size)
x, y좌표로부터 size만큼의 정사각형의 파란색과 하얀색 정사각형 갯수를 세서
    튜플로(white_cnt, blue_cnt)로 반환하는 함수다.
white_cnt, blue_cnt = solve(0, 0, size)
1. 만약 전부 하얀색이라면? return (1, 0)
2. 만약 전부 파란색이라면? return (0, 1)
3. 4방으로 쪼갠다.
각각의 쪼개진 정사각형에서 센 (white_cnt, blue_cnt)를 전부 합하면 그게 정답이다.
w1, b1 = solve(x, y, size//2)
w2, b2 = solve(x, y+size//2, size//2)
w3, b3 = solve(x+size//2, y, size//2)
w4, b4 = solve(x+size//2, y+size//2, size//2)
return (w1+w2+w3+w4, b1+b2+b3+b4)
'''


def solve(x,y,size):
    global white, blue

    color = board[x][y]

    for i in range(x, x+ size):
        for j in range(y, y+ size):
            if(board[i][j] != color):
                half = size // 2
                solve(x, y, half)
                solve(x, y + half, half)
                solve(x + half, y, half)
                solve(x + half, y + half, half)
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1





if __name__ == "__main__":
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    white = 0
    blue = 0

    solve(0,0,N)

    print(white)
    print(blue)