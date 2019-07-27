class Solution:
    def maxProfit(self, prices):
        length = len(prices)

        dp_0 = 0
        dp_1 = -9999
        dp_pre = 0

        for i in range(length):
            temp = dp_0
            dp_0 = max(dp_0,dp_1+prices[i])
            dp_1 = max(dp_1,dp_pre - dp_pre)
            dp_pre = temp

        return dp_0

if __name__ == '__main__':
    so = Solution()
    res = so.maxProfit([1,2,3,0,2])
    print(res)
