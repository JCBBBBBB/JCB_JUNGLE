# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478
import sys



# n(몇번 반복할지), original(처음의 n을 저장), add('____' 문자열 기본값 저장)
def recur(n, original, add = "____"): 
    #n이 줄어들게 재귀로 설계

    # 처음 한번만 실행
    if(n == original): # n이 original(원래의 n)이면
        print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
        print("\"재귀함수가 뭔가요?\"")
        print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
	
    # 마지막에 한번만 실행
    elif(n == 0):
        add = "____" * (original - n)    #매개변수로 받은 처음 n(original) 에서 현재의 n뺀 수를 곱해 '____'문자열 개수 나타낸다
        print(f"{add}\"재귀함수가 뭔가요?\"")
        print(f"{add}\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(f"{add}라고 답변하였지.")
        return #마지막에 return

    # 처음과 마지막이 아닐때 계속 실행된다
    else:
        add = "____" * (original - n) 
        print(f"{add}\"재귀함수가 뭔가요?\"")
        print(f"{add}\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print(f"{add}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print(f"{add}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")

    # n-1 재귀
    recur(n-1, original)

    # n==0에서 return 되고 여기로 온다
    add = "____" * (original - n) 
    print(f"{add}라고 답변하였지.")


if __name__ == "__main__":
    n = int(input())
    recur(n, n)