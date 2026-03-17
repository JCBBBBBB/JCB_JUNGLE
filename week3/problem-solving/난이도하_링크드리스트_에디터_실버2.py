# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

from collections import deque



#abcd
entire = input().split()


left = deque(entire[0])
right = deque()

#3
num = int(input())

for i in range(num):
    data = input().split()

    if(data[0] == 'L'):
        if(left):
            right.appendleft(left.pop())
    if(data[0] == 'D'):
        if(right):
            left.append(right.popleft())
    if(data[0] == 'B'):
        if(left):
            left.pop()
    if(data[0] == 'P'):
        left.append(data[1])

# answer = ''
# for part in left + right:
#     answer += part


# 사용 이유: 한번에 최종 문자열을 생성하여 시간이 빠름
print(''.join(left+right))