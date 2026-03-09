# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819


#수의 개수 입력받는다
N = int(input())

num_list = list()

# 수를 입력받아 리스트에 저장한다
for i in range(N):
    data = list(map(int, input().split()))
    num_list.append(data[0])


#수를 정렬한다
for i in range(N-1):
    temp_num = num_list[i]
    for j in range(i+1, N):
        if(temp_num>= num_list[j]):
            temp_num = num_list[j]
    for k in range(i+1, N):
        if(num_list[k] == temp_num):
            num_list[i], num_list[k] = num_list[k], num_list[i]

#num_list에 일단 최솟값 순서대로 저장을 시켰다.

new_list = [None] * N
#[1,2,3,4,5]
#홀수
if(N % 2 == 1):
    even_num = 0
    odd_num = 1

    # (N + 1) / 2가 큰거
    # N - (N+1) / 2가 작은거 
    #인덱스 맨 뒤부터 0까지 역순으로 내려간다
    big_for_num = (N+1) / 2    #N이 5일 때 3
    small_for_num = N - ((N+1) / 2) #N이 5일 때 2

    big_for_num = int(big_for_num)
    small_for_num = int(small_for_num)


    for i in range(N-1, (N-1)- (big_for_num), -1): # 4 부터 2까지 
        new_list[even_num] = num_list[i]
        even_num += 2
    for j in range(small_for_num-1, -1, -1): #2부터 0까지
        new_list[odd_num] = num_list[j]
        odd_num += 2


print(num_list)