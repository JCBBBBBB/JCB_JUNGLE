"""
[정수론 - 최대공약수(GCD)와 최소공배수(LCM)]

문제 설명:
- 두 정수의 최대공약수(GCD)와 최소공배수(LCM)를 구합니다.
- 유클리드 호제법을 사용하여 GCD를 효율적으로 계산합니다.
- GCD를 이용하여 LCM을 계산합니다.

입력:
- a, b: 두 개의 양의 정수

출력:
- GCD: 최대공약수
- LCM: 최소공배수

예제:
입력: a = 48, b = 18
출력: 
  GCD = 6
  LCM = 144

힌트:
- 유클리드 호제법: gcd(a, b) = gcd(b, a % b)
- LCM 공식: lcm(a, b) = (a × b) / gcd(a, b)
"""

def gcd(a, b):
    """
    유클리드 호제법을 사용한 최대공약수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최대공약수 
    """

    #큰 수에서 작은 수 나눠서    ... 나머지
    #나머지 0 아니면 나눠지는 수를 나머지로 나눈다
    #나머지 0이면 나눠지는 몫이 최대공약수

    #예시 (48, 18)
    # 48 % 18 = 2 ... 12
    # 18 % 12 = 1 ... 6
    # 12 % 6 = 2 ... 0 -> 나머지가 0이므로 최대공약수는 6



    max_num = max(a,b) # 큰 수
    min_num = min(a,b) # 작은 수

    temp_num = max_num % min_num # 큰 수와 작은 수를 나누었을 때의나머지
    answer = 0 # 최대공약수

    while True: # 나머지가 0이 나올때까지

        if(temp_num != 0): # 나머지가 0이 아니면
            max_num = min_num
            min_num = temp_num
            temp_num = max_num % min_num #나눠지는 수를 나머지로 나눈다
        else: # 나머지가 0이면
            answer = min_num
            break

    return answer




    # TODO: 유클리드 호제법 구현
    # base case: b가 0이면 a 반환
    # recursive를 이용 
    

def gcd_iterative(a, b):
    """
    반복문을 사용한 최대공약수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최대공약수
    """

    # a,b의 공약수들을 담을 리스트 생성
    a_remain_list = list()
    b_remain_list = list()

    # a,b의 최대공약수를 담을 리스트 생성
    common_divisor = list()

    # a 인덱스까지 for문을 돌며 나머지가 0인것들을 리스트에 넣는다
    for i in range(1, a+1):
        if(a % i == 0):
            a_remain_list.append(i)

    # b 인덱스까지 for문을 돌며 나머지가 0인것들을 리스트에 넣는다
    for i in range(1, b+1):
        if(b % i == 0):
            b_remain_list.append(i)

    # a 리스트를 기준으로 b 리스트 인덱스들을 돌면서 서로 같은 것들을 리스트에 넣는다 -> 공약수 넣는 것!
    for i in range(len(a_remain_list)):
        for j in range(len(b_remain_list)):
            if(a_remain_list[i] == b_remain_list[j]):
                common_divisor.append(a_remain_list[i])

    # 거기서 가장 큰 게 최대공약수
    answer = max(common_divisor)



    return answer







    # TODO: 반복문으로 구현
    # b가 0이 될 때까지 반복
    

def lcm(a, b):
    """
    최소공배수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최소공배수
    """
    # TODO: LCM 계산

    gcd_num = gcd(a,b) #최대공약수 계산

    # 각 수를 최대공약수로 나눈다
    a_divide_gcd = a / gcd_num
    b_divide_gcd = b / gcd_num

    # 최대공약수와 저 값들을 곱한다
    lcm_num = gcd_num * a_divide_gcd * b_divide_gcd

    return int(lcm_num)
    

def extended_gcd(a, b):
    """
    확장 유클리드 호제법
    ax + by = gcd(a, b)를 만족하는 x, y를 찾음
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        (gcd, x, y) 튜플
    """
    # TODO: 확장 유클리드 호제법 구현
    # base case: b가 0이면 (a, 1, 0) 반환    
    # recursive case
    # 역추적하며 x, y 계산
    pass

def is_prime(n):
    """
    소수 판별
    
    Args:
        n: 판별할 양의 정수
    
    Returns:
        소수이면 True, 아니면 False
    """
    #약수 리스트
    decide_list = list()

    #1부터 자기자신 인덱스까지 돌면서
    for i in range(1, n+1):
        if(n % i == 0): #i로 나눠지는 거를
            decide_list.append(i) #리스트에 넣는다

    if(len(decide_list) == 2): #개수가 2개면 소수이다
        return True
    else:
        return False


    # TODO: 소수 판별 구현
    # n이 2보다 작으면 False
    # 2부터 sqrt(n)까지 나누어 떨어지는지 확인    
    # 3부터 sqrt(n)까지 홀수만 확인
    pass 

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: GCD와 LCM
    print("=== 테스트 케이스 1: GCD와 LCM ===")
    a, b = 8, 48
    print(f"a = {a}, b = {b}")
    print(f"GCD (재귀): {gcd(a, b)}")
    print(f"GCD (반복): {gcd_iterative(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    a, b = 100, 75
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 3: 서로소
    print("=== 테스트 케이스 3: 서로소 ===")
    a, b = 17, 19
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print("서로소(coprime): GCD가 1")
    print()
    
    # 테스트 케이스 4: 확장 유클리드
    print("=== 테스트 케이스 4: 확장 유클리드 ===")
    a, b = 35, 15
    g, x, y = extended_gcd(a, b)
    print(f"a = {a}, b = {b}")
    print(f"GCD = {g}")
    print(f"{a} × {x} + {b} × {y} = {g}")
    print(f"검증: {a * x + b * y} = {g}")
    print()
    
    # 테스트 케이스 5: 소수 판별
    print("=== 테스트 케이스 5: 소수 판별 ===")
    test_numbers = [2, 3, 4, 17, 20, 29, 100]
    for num in test_numbers:
        result = "소수" if is_prime(num) else "합성수"
        print(f"{num}: {result}")


