class Solution:
    def maxProfit(self,prices):
        length = len(prices)
        k = 2
        if length < 2:
            return  0

        if k < length//2:
            dp = [[-prices[0],0] for _ in range(k+1)]
            for price in prices[1:]:
                for i in range(1,k+1):
                    dp[i][0] = max(dp[i][0],dp[i-1][1]-price)
                    dp[i][1] = max(dp[i][1],dp[i][0]+price)
            return dp[k][1]
        else:
            dp = [-prices[0],0]
            for price in prices[1:]:
                dp = [max(dp[0],dp[1]-price),max(dp[1],dp[0]+price)]
            return dp[1]