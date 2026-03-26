# 그래프, BFS - Word Ladder
# 문제 링크: https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150


def dfs(graph, start):
    visited = []
    back_edges = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                else:
                    back_edges.add((node, neighbor))
        else:
            continue

    return visited, sorted(list(back_edges))


if __name__ == "__main__":
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'G': ['H'],
    'H': ['F'],
  }
    
    print(dfs(graph, 'A'))