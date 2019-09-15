class Solution:
    # def maxProfit(self,prices):
    #     length = len(prices)
    #     k = 2
    #     if length < 2:
    #         return  0
    #
    #     if k < length//2:
    #         dp = [[-prices[0],0] for _ in range(k+1)]
    #         for price in prices[1:]:
    #             for i in range(1,k+1):
    #                 dp[i][0] = max(dp[i][0],dp[i-1][1]-price)
    #                 dp[i][1] = max(dp[i][1],dp[i][0]+price)
    #         return dp[k][1]
    #     else:
    #         dp = [-prices[0],0]
    #         for price in prices[1:]:
    #             dp = [max(dp[0],dp[1]-price),max(dp[1],dp[0]+price)]
    #         return dp[1]

    # second
    def maxProfit(self, prices):
        size = len(prices)
        k= 2
        if size < 2:return 0

        if k < size//2:
            dp = [[-prices[0],0] for _ in range(k+1)]
            for price in prices[1:]:
                for i in range(1,k+1):
                    #在买入股票时，计 交易次数
                    dp[i][0] = max(dp[i][0],dp[i-1][1]-price)
                    dp[i][1] = max(dp[i][1],dp[i][0] + price)

            return dp[k][1]
        else:
            dp = [-prices[0],0]
            for price in prices[1:]:
                dp = [max(dp[0],dp[1]-price),max(dp[1],dp[0] + price)]
            return dp[1]

if __name__ == '__main__':
    so = Solution()
    print(so.maxProfit([1,2,4,2,5,7,2,4,9,0]))