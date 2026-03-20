"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO: visited가 None이면 초기화
    if(visited == None):
        visited = []
    
    # TODO: 현재 정점 방문
    stack = [] #방문 처리 할 스택 생성

    stack.append(start) #stack에 현재 위치 추가
    visited.append(start) #visited에 현재 위치 방문 처리
    
    # TODO: 인접한 정점들에 대해 재귀
    ## 방문하지 않은 정점이면 재귀 호출
    while(stack):
        cur = stack.pop() #스택의 마지막 pop

        for nx in graph[cur]:
            if(nx < 0 or nx > 3):
                continue
            if(nx not in visited): #nx가 visited에 없으면
                stack.append(nx)
                visited.append(nx)
    
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


