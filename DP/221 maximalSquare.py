class Solution:
    #典型的动态规划题目，
    #在matrix[i][j] == '1'时，
    # 判断 dp(i, j) = min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1
    #通过选择最小，省的取判读 多出来的列或行 是否有满足要求的'1'，因为使用的是最小，所以多出来的列，行符合要求

    def maximalRectangle(self, matrix):
        row = len(matrix)
        col = 0
        #先判断是否有行，再判断列
        if row:
            col = len(matrix[0])
        if not row or not col:
            return 0

        dp = [0]*(col+1)
        pre = 0
        max_ = 0

        for i in range(1,row+1):
            for j in range(1,col+1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j], dp[j - 1], pre)+1
                    max_ = max(max_, dp[j])
                else:
                    dp[j] = 0
                pre = temp

        return max_ ** 2



if __name__ == '__main__':
    so = Solution()
    matrix = [['1',0,'1',0,0],
              ['1',0,'1','1','1'],
              ['1','1','1','1','1'],
              ['1',0,0,'1',0]]
    res = so.maximalRectangle(matrix)
    print(res)



