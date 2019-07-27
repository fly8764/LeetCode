class Solution:
    def maxProfit(self, prices):
        length = len(prices)

        dp_0 = 0
        dp_1 = -99999

        for i in range(length):
            temp = dp_0
            dp_0 = max(dp_0,dp_1+prices[i])
            dp_1 = max(dp_1,temp-prices[i])

        return dp_0

if __name__ == '__main__':
    so = Solution()
    res = so.maxProfit([7,1,5,3,6,4])
    print(res)



