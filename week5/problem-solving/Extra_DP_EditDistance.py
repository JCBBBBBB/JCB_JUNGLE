# DP - Edit Distance
# 문제 링크: https://leetcode.com/problems/edit-distance/description/?envType=study-plan-v2&envId=top-interview-150




d = [0] * 1000005

d[1] = 0

num = int(input())

for i in range(2, num + 1):
    d[i] = d[i-1] + 1
    if(i % 2 == 0):
        d[i] = min(d[i], d[int(i/2)] + 1)
    if(i % 3 == 0):
        d[i] = min(d[i], d[int(i/3)] + 1)

print(d[num])
