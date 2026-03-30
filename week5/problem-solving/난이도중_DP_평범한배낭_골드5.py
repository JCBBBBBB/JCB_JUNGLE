# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for w, v in items:
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
    
print(dp[K])