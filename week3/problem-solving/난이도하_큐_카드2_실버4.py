# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

# q = []

# while(len(q) != 1):
#     q.pop(0) #배열에서 삭제하는 거기때문에 시간복잡도가 n이다 -> 시간 오래 걸린다
#     q.append(q[0]) 
#     q.pop(0) #배열에서 삭제하는 거기때문에 시간복잡도가 n이다 -> 시간 오래 걸린다



from collections import deque

num = int(input())

q = deque() # 내장 deque 사용

for i in range(1, num+1): # q에 1~n까지 숫자 삽입
    q.append(i)

while(len(q) != 1): # 큐의 개수가 1개가 아닐때만 반복문 실행
    q.popleft() # 큐의 처음을 삭제한다
    q.append(q[0])
    q.popleft() # 큐의 처음을 삭제한다

print(len(q))
print(q[0])
