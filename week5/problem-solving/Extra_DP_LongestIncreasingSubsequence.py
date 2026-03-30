# DP - Longest Increasing Subsequence
# 문제 링크: https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-interview-150



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        #abbbcdeeff
        #ef bbb     fe 홀수중에 제일 많은거 + 짝수 다 더하기


        data = set(s)

        dict = {item: 0 for item in data}

        for word in s:
            dict[word] += 1

        answer = 0
        odd_list = list()

        for value in dict.values():
            if(value % 2 == 0):
                answer += value
            else:
                odd_list.append(1)
                answer += (value-1)

        if(odd_list):
            answer += 1

        print(answer)


if __name__ == "__main__":
    solution = Solution()
    solution.longestPalindrome("a")