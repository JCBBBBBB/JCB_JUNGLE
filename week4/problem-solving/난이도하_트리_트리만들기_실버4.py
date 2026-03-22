# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
n, m = map(int, input().split())

# 4,3   3,2   5,3
#n = 노드, m = 리프 개수
# 0번에 1~m 붙이기
for i in range(1, m + 1):
    print(0, i)

# 남는 정점들은 m번 뒤에 체인처럼 붙이기
for i in range(m + 1, n):
    print(i - 1, i)