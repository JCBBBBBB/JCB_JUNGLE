# 배열 - H-Index
# 문제 링크: https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

def departure_day(n): 
	
    if(n <1 ):
      return
    return departure_day(n-1)


if __name__ == "__main__":
        print(departure_day(7))