class Solution1:
    #动态规划 贪心结论 滚动数组
    def integerBreak(self, n):
        dp = [0,1,1]
        for i in range(3,n+1):
            dp[i%3] = max(1*max(dp[(i-1)%3],i-1),2*max(dp[(i-2)%3],i-2),3*max(dp[(i-3)%3],i-3))
        return dp[n%3]
    #动态规划 贪心结论
    # max(dp[i-1],i-1) 对i-1 继续分割 和不分割
    # def integerBreak(self, n):
    #     dp = [0]*(n+1)
    #     dp[1],dp[2] = 1,1
    #     for i in range(3,n+1):
    #         dp[i] = max(1*max(dp[i-1],i-1),2*max(dp[i-2],i-2),3*max(dp[i-3],i-3))
    #
    #     return dp[-1]

    #常规 动态规划
    # def integerBreak(self, n):
    #     dp = [0]*(n+1)
    #     dp[1],dp[2] = 1,1
    #     for i in range(3,n+1):
    #         for j in range(1,i):
    #             dp[i] = max(dp[i],dp[j]*(i-j),j*(i-j))
    #
    #     return dp[n]

class Solution:
    def integerBreak(self, n):
        pass

if __name__ == '__main__':
    so = Solution()
    res = so.integerBreak(10)
    print(res)

