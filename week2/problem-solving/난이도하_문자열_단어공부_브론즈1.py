# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 대소문자 구분 X

#입력 : 첫째줄에 알파벳 대소문자로 이루어진 단어가 주어진다


# 출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다




#입력 예시 : Mississipi   출력 :   m : 1   i :4  s : 4 p :1
#입력 예시 : zZa 출력 Z

#내가 생각한 풀이 방법? : 



import sys
input = sys.stdin.readline

s = str(input())
s = s.upper()
my_dict = dict()

alphabet = set(s)
alphabet.remove('\n')

my_list = list(alphabet)

for i in range(len(alphabet)):
    my_dict[my_list[i]] = 0


for i in range(len(s)):
    if(s[i] == '\n'):
        break
    my_dict[s[i]] += 1

value_list = []
for value in my_dict.values():
    value_list.append(value)

max_value = max(value_list)

num = 0
for i in range(len(value_list)):
    if(value_list[i] == max_value):
        num += 1

if(num > 1):
    print('?')
else:
    for i in range(len(my_dict)):
        if(my_dict[s[i]] == max_value):
            print(s[i])
            break

# for value in my_dict.values():
#     print(value)