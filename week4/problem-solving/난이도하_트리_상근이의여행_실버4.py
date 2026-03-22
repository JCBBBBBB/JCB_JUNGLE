# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372


from collections import deque

T = int(input())



for i in range(T):
    N, M = list(map(int, input().split()))
    graph = {} #딕셔너리 형태로 갈 수 있는 곳 리스트
    visited = [] #방문한 곳 추가
    queue = deque() #로직 돌릴 큐
    answer = 0 #최소 비행기 수
    for j in range(M):
        a,b = list(map(int, input().split()))
        graph.setdefault(a, []).append(b) # 경로 양방향 추가
        graph.setdefault(b, []).append(a) # 경로 양방향 추가

    keys = list(graph.keys()) # 그래프 경로의 키 리스트
    if(graph[keys[0]]): # 그래프 경로의 첫번째 키의 값이 있으면
        queue.append(keys[0]) # 큐에 그 정점을 추가한다
        visited.append(keys[0]) # visited에도 그 정점을 추가한다

    while(queue): # 큐가 있으면
        cur = queue.popleft() #현재 위치 pop하고

        for next in graph[cur]: # 그 위치로 갈 수 있는 경로 중에서
            if(next not in visited): #방문 하지 않았으면
                queue.append(next) #큐에 추가
                visited.append(next) # visited에 추가
                answer += 1 #answer + 1

    print(answer)
    