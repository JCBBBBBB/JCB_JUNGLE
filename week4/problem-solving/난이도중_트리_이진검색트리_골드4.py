# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

# 배열로 관리
# 작으면

import sys

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    cur = root

    while True:
        if value < cur.value:
            if cur.left is None:
                


def postorder(node):
    if node is None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.value)

nums = []
for line in sys.stdin:
    nums.append(int(line.strip()))

root = Node(nums[0])

for num in nums[1:]:
    insert(root, num)

postorder(root)