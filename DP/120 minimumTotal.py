class Solution:
    #自底向上 dp[i] = min(dp[i],dp[i+1]) + nums[i]
    def minimumTotal(self, triangle):
        if not len(triangle) or not len(triangle[0]):
            return
        row = len(triangle)
        dp = []
        for i in range(len(triangle[-1])):
            dp.append(triangle[-1][i])

        for i in range(row-2,-1,-1):
            for j in range(1+i):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
        return dp[0]


    #从上到下 转移方程 cur[i] = min(dp[i-1],dp[i]) + nums[i]
    # def minimumTotal(self, triangle):
    #     if not len(triangle) or not len(triangle[0]):
    #         return
    #     cur,dp = [],[0]
    #     for nums in triangle:
    #         size = len(nums)
    #         cur = [0] *size
    #         for i in range(size):
    #             if i == 0:
    #                 cur[i] = dp[0] + nums[0]
    #             elif i == size-1:
    #                 cur[i] = dp[i-1]+ nums[i]
    #             else:
    #                 cur[i] = min(dp[i-1],dp[i]) + nums[i]
    #         dp = cur
    #     return min(dp)


if __name__ == '__main__':
    so = Solution()
    triangle  = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]]

    res = so.minimumTotal(triangle)
    print(res)


