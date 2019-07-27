class Solution:
    def maxProfit(self, prices, fee):
        length = len(prices)

        if length < 2:
            return 0

        dp = [-prices[0], 0]
        for price in prices[1:]:
            dp = [max(dp[0], dp[1] - price), max(dp[1], dp[0] + price - fee)]
        return dp[1]