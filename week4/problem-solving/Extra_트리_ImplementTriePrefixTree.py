# 트리 - Implement Trie (Prefix Tree)
# 문제 링크: https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150

from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        queue = deque()
        visited = [[False] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        answer = 0

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == '1' and not visited[i][j]): #섬이고 아직 방문하지 않았으면
                    queue.append((i,j))
                    visited[i][j] = True

                    while(queue):
                        x,y = queue.popleft() #현재 위치

                        for dir in range(4):
                            nx = x + dx[dir]
                            ny = y + dy[dir]
                            if(nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0])):
                                continue
                            if(visited[nx][ny]):
                                continue
                            if(grid[nx][ny] == '0'): #이걸 왜 처리해야 되나? 0이면 
                                continue

                            queue.append((nx,ny))
                            visited[nx][ny] = True
                    
                    answer += 1
        return answer

if __name__ == "__main__":
    solution = Solution()
    grid = [  ["1","1","0","0","0"], 
  ["1","1","0","0","0"], 
  ["0","0","1","0","0"], 
  ["0","0","0","1","1"] ] 
    solution.numIslands(grid )