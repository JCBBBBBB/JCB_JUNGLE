# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

# ai 힌트 사용, 코드 x

# 투포인터 사용 

# 전체 용액의 수
N = int(input())


# -2 4 - 99 -1 98
data = list(map(int, input().split()))


data.sort() # -99 -2 -1 4 98


l = 0 # 왼쪽 인덱스
r = len(data) - 1 # 오른쪽 인덱스
sum = data[l] + data[r] #맨 왼쪽 + 맨 오른쪽 합
leftNum = data[l]
rightNum = data[r]


while(l < r):
    if(data[l] + data[r] < 0):
        l += 1
        if(l >= r):
            break
        if(abs(sum) > abs(data[l] + data[r])):
            leftNum = data[l]
            rightNum = data[r]
            sum = data[l] + data[r]

    elif(data[l] + data[r] > 0):
        r -= 1
        if(l >= r):
            break
        if(abs(sum) > abs(data[l] + data[r])):
            leftNum = data[l]
            rightNum = data[r]
            sum = data[l] + data[r]
    else:
        leftNum = data[l]
        rightNum = data[r]
        break

minNum = min(leftNum, rightNum)
maxNum = max(leftNum, rightNum)

print(minNum, maxNum)