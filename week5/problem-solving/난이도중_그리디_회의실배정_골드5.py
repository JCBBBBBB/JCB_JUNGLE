# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

N = int(input())

meeting_list = list() #회의 담을 리스트

for i in range(N):
    start, end  = map(int, input().split())
    meeting_list.append((start,end)) #회의 추가

meeting_list = sorted(meeting_list, key = lambda x: (x[1], x[0])) # 끝나는 시간으로 정렬

if(meeting_list[0]):
    answer = 1 #최대 사용할 수 있는 회의의 최대 개수, 처음 것이 있다면 1로 설정을 한다
    temp = meeting_list[0][1]


#회의 수 돌면서
for i in range(1, N):
    #회의의 시작시간이 전 회의의 끝나는 시간보다 크거나 같으면
    if(meeting_list[i][0] >= temp):
        answer += 1
        temp = meeting_list[i][1] #temp는 현재 회의의 끝나는 시간이 된다

print(answer)