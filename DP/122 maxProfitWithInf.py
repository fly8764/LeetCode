'''
方法一：动态规划(系类题通用解法)
方法二：贪心算法(该题的考察点),只要当天的股价比昨天的高，就卖出，
一天之内，可以 卖和买先后进行。
'''
class Solution:
    #second
    # def maxProfit(self, prices):
    #     #贪心，只要今天比昨天的股价高，就交易
    #     size = len(prices)
    #     profit = 0
    #     for i in range(1,size):
    #         if prices[i] > prices[i-1]:
    #             profit += prices[i] - prices[i-1]
    #
    #     return profit

    def maxProfit(self, prices):
        size = len(prices)
        dp_0 = 0
        dp_1 = float('-inf')

        for i in range(size):
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, dp_0 - prices[i])

        return dp_0


    # def maxProfit(self, prices):
    #     length = len(prices)
    #
    #     dp_0 = 0
    #     dp_1 = -99999
    #
    #     for i in range(length):
    #         temp = dp_0
    #         dp_0 = max(dp_0,dp_1+prices[i])
    #         dp_1 = max(dp_1,temp-prices[i])
    #
    #     return dp_0

if __name__ == '__main__':
    so = Solution()
    res = so.maxProfit([7,1,5,3,6,4])
    print(res)



