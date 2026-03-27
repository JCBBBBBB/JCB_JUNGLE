# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748


n = int(input())


d = [0] * (n+5)


d[0] = 0
d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])



