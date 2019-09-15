'''
思路：
方法一：
方法二：动态的选取 当前的最大收益 和当前的最小价格(为后面的服务)
当前最大收益 等于 max(当前收益，当前价格与之前最小价格差)
这个当前最大收益和当前最小价格 分别使用一个变量保存当前情况即可，
不需要保存之前的情况，保存了也用不到
'''
#second
class Solution:
    def maxProfit(self, prices):
        size = len(prices)
        if size < 2:return 0
        profit = 0

        # min_price = float('-inf') #用负数来表示
        # for i in range(size):
        #     profit = max(profit,prices[i] + min_price)
        #     min_price = max(min_price,-prices[i]) #绝对值最小
        # return profit

        min_price = float('inf')  # 用整数来表示
        for i in range(size):
            profit = max(profit,prices[i] - min_price)
            min_price = min(min_price,prices[i])
        return profit

    # def maxProfit(self, prices):
    #     size = len(prices)
    #     if size < 2:return 0
    #     dp = [0]*size
    #     #dp[i]：代表到prices[i]为止的最大收益
    #     for i in range(1,size):
    #         #这种方式里面的max() 和min()在数据量大时，容易超时
    #         #最小价格使用一个变量保存，实时更新即可，使用一个数组保存，查询时耗时
    #         dp[i] = max(max(dp[i-1]),prices[i]- min(prices[:i]))
    #     return dp[-1]


if __name__ == '__main__':
    so = Solution()
    print(so.maxProfit([7,1,5,3,6,4]))
    print(so.maxProfit([7,6,4,3,1]))

# class Solution:
#     def maxProfit(self, prices):
#         length = len(prices)
#
#         dp_0 = 0
#         dp_1 = -999999
#
#         for i in range(length):
#             dp_0 = max(dp_0,dp_1 + prices[i])
#             dp_1 = max(dp_1,-prices[i])
#         return dp_0
#
#
#     def maxProfit1(self, prices):
#         length = len(prices)
#
#         min_p = 99999
#         profit = 0
#
#         for i in range(length):
#             if prices[i]< min_p:
#                 min_p = prices[i]
#             elif prices[i]-min_p > profit:
#                 profit = prices[i] - min_p
#         return profit
#
#
# if __name__ == '__main__':
#     so = Solution()
#     res = so.maxProfit([7,1,5,3,6,4])
#     print(res)
#
