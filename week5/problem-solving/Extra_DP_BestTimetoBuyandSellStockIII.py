# DP - Best Time to Buy and Sell Stock III
# 문제 링크: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        d = [0] * (n+5)

        d[1] = 1
        d[2] = 2

        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]

        return d[n]

    
if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))