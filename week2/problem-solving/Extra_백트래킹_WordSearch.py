# 백트래킹 - Word Search
# 문제 링크: https://leetcode.com/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150

def myPow(x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(n > 0):
            for i in range(n-1):
                x *= x
        elif(n < 0):
            x = 1/x
            for i in range(n-1):
                x *= x
        else:
            return 1

        return x


print(myPow(2,10))