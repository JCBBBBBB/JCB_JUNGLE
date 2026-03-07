# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344



import sys
input = sys.stdin.readline



test_case = int(input())



for i in range(test_case):
    
    data = list(map(int, input().split())) #이렇게 해야된다 파이썬은
    student_num = data[0]
    student_list = data[1:]
    average_score = sum(student_list) / student_num

    count = 0
    for k in range(student_num):
        if(student_list[k] > average_score):
            count += 1

    answer = (count / student_num) * 100
    print(f'{answer:.3f}%')
