# DP - Edit Distance
# 문제 링크: https://leetcode.com/problems/edit-distance/description/?envType=study-plan-v2&envId=top-interview-150
//
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # num = len(triangle) #ex) 4

        # sum = 0
        # for i in range(len(triangle)):
        #     sum += min(triangle[i])

        # return sum

        #i행 j열에서의 행의 인접한 인덱스의 최소 합
        #d[i][j] = min(d[i-1][j-1], d[i-1][j]) + triangle[i][j]
        num = len(triangle)
        d = [[0] * (num) for _ in range(num+1)]

        if(num == 1):
            return triangle[0][0]

        
        d[1][0] = triangle[0][0] + triangle[1][0]
        d[1][1] = triangle[0][0] + triangle[1][1]

        for i in range(2, num):
            for j in range(len(triangle[i])):
                    if j == 0:
                        d[i][j] = d[i-1][0] + triangle[i][j]
                    elif j == len(triangle[i]) - 1:
                        d[i][j] = d[i-1][len(triangle[i]) - 2] + triangle[i][j]
                    else:
                        d[i][j] = min(d[i-1][j-1], d[i-1][j]) + triangle[i][j]

        new_triangle_row = d[num-1][:]
        return min(new_triangle_row)



if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))