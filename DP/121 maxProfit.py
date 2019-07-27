class Solution:
    def maxProfit(self, prices):
        length = len(prices)

        dp_0 = 0
        dp_1 = -999999

        for i in range(length):
            dp_0 = max(dp_0,dp_1 + prices[i])
            dp_1 = max(dp_1,-prices[i])
        return dp_0


    def maxProfit1(self, prices):
        length = len(prices)

        min_p = 99999
        profit = 0

        for i in range(length):
            if prices[i]< min_p:
                min_p = prices[i]
            elif prices[i]-min_p > profit:
                profit = prices[i] - min_p
        return profit


if __name__ == '__main__':
    so = Solution()
    res = so.maxProfit([7,1,5,3,6,4])
    print(res)

