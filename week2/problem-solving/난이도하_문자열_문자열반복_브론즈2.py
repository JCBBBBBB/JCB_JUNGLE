# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675




import sys
input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    repeat_num, temp_string = input().split()

    repeat_num = int(repeat_num)

    #문자열
    answer = ""
    for j in range(len(temp_string)):
        for k in range(repeat_num):
            answer += temp_string[j]

    print(answer)