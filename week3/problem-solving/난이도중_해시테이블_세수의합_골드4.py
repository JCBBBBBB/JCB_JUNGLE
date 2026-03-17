# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

#x+y 가능한 모든값 저장
#d 큰거부터 본다
#d마다 z하나씩 넣어본다
#d-z == x+y 이면 처음 d 출력

#시간복잡도 : O(N제곱) -> 가능  1000 * 1000
#x+y+z = d -> x+y = d-z
#3중 for문 안쓰고 2중 for문으로 가능해진다

def function():
#리스트에 넣는다
    for i in range(N):
        temp_num = int(input())
        element_list.append(temp_num)



    #정렬한다 -> 이유 ? 나중에 가장 큰 d부터 찾을라고
    element_list.sort()

    for i in range(N):
        for j in range(N):
            sum_set.add(element_list[i] + element_list[j])

    #이제 set 에는 {5,7,12,20, 8 ...} 이런 값이 있다
    for i in range(N-1, 0, -1):
        for j in range(i-1, -1, -1):
            if(element_list[i] - element_list[j]) in sum_set:
                print(element_list[i])
                return





if __name__ == "__main__":
    N = int(input())

    element_list = list()
    sum_set = set()

    function()