# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920






def find_target():
    for target in arr_m:
        left = 0
        right = len(arr_n) - 1
        define_num = 0

        while(left <= right):
            mid = int((left + right) / 2)

            if(arr_n[mid] == target):
                define_num = 1
                print(define_num)
                break
            elif(arr_n[mid] > target):
                right = mid - 1
            elif(arr_n[mid] < target):
                left = mid + 1

        if(define_num == 0):
            print(define_num)

if __name__ == "__main__":

    n = int(input()) #자연수

    arr_n = list(map(int, input().split())) #밑에서 받은 수를 여기서 찾아야 함
    arr_n.sort()

    m = int(input())

    arr_m = list(map(int, input().split())) #여기 있는 수를 찾아야함

    find_target()