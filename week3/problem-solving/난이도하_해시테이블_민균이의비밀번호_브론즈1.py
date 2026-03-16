# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933





def function():
    for i in range(num):
        word = input() #단어 input 받는다

        word_list.append(word) #단어 word_list에 추가한다

    for i in word_list:
        temp = i[::-1] # 문자 뒤집음
        for j in word_list:
            if(temp == j):
                print(len(j), j[len(j) // 2])
                return
            
if __name__ == "__main__":
    # 단어의 수
    num = int(input())


    word_list = list()

    function()
