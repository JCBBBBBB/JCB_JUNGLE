# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

num = int(input())

stack = []



while num > 0:
    text = input().split()
    num -=1

    if(text[0] == 'push'):
        stack.append(int(text[1]))
    elif(text[0] == 'pop'):
        if not stack:
                print(-1)
        else:              
            print(stack.pop())
    elif(text[0] == 'size'):
        print(len(stack))
    elif(text[0] == 'empty'):
        if not stack:
                print(1)
        else:
            print(0)
    elif(text[0] == 'top'):
        if stack:
            print(stack[-1])
        else:
            print(-1)


    # match text.split():
    #     case ['push', x]:
    #         stack.append(int(x))
    #     case ['pop']:
    #         if not stack:
    #             print(-1)
    #         else:              
    #             print(stack.pop())
    #     case ['size']:
    #         print(len(stack))
    #     case ['empty']:
    #         if not stack:
    #             print(1)
    #         else:
    #             print(0)
    #     case ['top']:
    #         if stack:
    #             print(stack[-1])
    #         else:
    #             print(-1)

