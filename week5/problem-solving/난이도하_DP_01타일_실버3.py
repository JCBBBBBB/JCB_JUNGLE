# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904



N = int(input())

d = [0] * 1000005

d[1] = 1
d[2] = 2

for i in range(3, N+1):
    d[i] = (d[i-1] + d[i-2]) % 15746

print(d[N])


