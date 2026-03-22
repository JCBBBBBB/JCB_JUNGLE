# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

N = int(input())

node_dict = dict()

for i in range(N-1):
    x, y = map(int, input().split())
    node_dict.setdefault(x, []).append(y)
    node_dict.setdefault(y, []).append(x)


for i in range(2, N+1):
    print(node_dict[i][0])