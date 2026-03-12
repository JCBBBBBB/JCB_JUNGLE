# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

from itertools import permutations
import sys
input = sys.stdin.readline

# #수의 개수 입력받는다
input = sys.stdin.readline  # 백준 스타일 입력으로 변경

num = int(input())

# 데이터 
data = list(map(int, input().split()))

max_sum = float('-inf')
#순열 돌면서
for perm in permutations(data):
    temp_num = perm[0] 
    result_sum = 0
    for i in range(len(perm)-1):
        temp_num = abs(perm[i] - perm[i+1])
        result_sum += temp_num

    max_sum = max(max_sum, result_sum)
    
print(max_sum)