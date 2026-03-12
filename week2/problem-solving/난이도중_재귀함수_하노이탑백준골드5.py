# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

# 원판 개수

#n개를 a에서 b를 거쳐 c로 보내야함
def hanoi(n, start, via, to):
    if(n == 1):
        print(start , to)
        return


    hanoi(n-1, start, to, via)
    print(start, to)
    hanoi(n-1, via, start, to)




if __name__ == "__main__":
    n = int(input())
    
    print(2**n - 1)
    if(n <=20):
        hanoi(n, 1,2,3)