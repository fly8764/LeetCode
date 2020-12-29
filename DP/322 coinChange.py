class Solution4:
    def coinChange(self, coins, amount):
        dp = [999999]*(amount+1)
        dp[0]= 0
        if amount == 0:
            return 0
        for i in range(amount+1):
            for coin in coins:
                if coin > i:
                    continue
                dp[i] = min(dp[i],1 + dp[i-coin])
        if dp[-1] == 999999:
            return -1
        else:
            return dp[-1]

        #类型二：找出最少的硬币——组成所有的面值
        #https://www.cnblogs.com/anzhengyu/p/11176134.html
        #其中，关于合适可以用一个硬币代替其中一个dp值应该满足的条件：
        #比如 dp[i] + dp[j] 只要i>=j-1,理论上dp[i]就可以组成[1,j-1]种所有值，
        #这种情况若j在硬币库中，则可以直接用一个硬币表示。

        #条件：i>=j-1
        #题目要求 能凑齐 amount内的所有面值，对应j，如果用一个硬币替代了，那么j-1(包括)
        #能不能凑齐呢？比如 7=5+2，用了硬币5，那4,3就没法凑齐，
        # 所以需要i>=j-1,让dp[i]来保证凑齐

class Solution2:
    def coinChange(self,coins,amount):
        if amount == 0:
            return 0
        dp = [float('inf')]*(amount +1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin > amount:
                    continue
                dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]

'''
变形，找出最少的硬币--组成所有的面值
https://www.cnblogs.com/anzhengyu/p/11176134.html
当可以用硬币直接替换时: dp[i] = min(dp[i-coin] +1,dp[i])
可以替换的条件是 i-j>= j-1,
把i分成两部分i-j,j 当j是一种硬币面值时，如果直接替换，要保证i-j能凑出
j-1的所有面值，即 i-j >= j-1,j直接用硬币即可
比如 7=5+2，用了硬币5，那4,3就没法凑齐，

当硬币不可以直接替换时 dp[i] = min(dp[i-j]+dp[j],dp[i])
'''
class Solution3:
    def coinChange(self,coin,target):
        pass

'''
2020/11/30 23:31
完全背包问题
dp[i][j]:前i个商品，达到价值j，用到的最少硬币数。
空间优化可以到一维。
其中两层循环有两种写法，一种是常规的完全背包问题写法。
另一种：第一层循环重量，第二层循环各种硬币，看当前重量下，使用哪种硬币可以使得用的硬币数量较少。
'''
class Solution:
    def coinChange(self, coins, amount):
        size = len(coins)
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(size):
            for j in range(coins[i],amount+1):
                dp[j] = min(dp[j],dp[j-coins[i]]+1)

        # for j in range(1,amount+1):
        #     for coin in coins:
        #         if coin <= j:
        #             dp[j] = min(dp[j], dp[j - coin]+1)
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]



if __name__ == '__main__':
    so = Solution()
    coins = [2] #[1, 2, 5]
    amount = 3  # 3 11
    res = so.coinChange(coins,amount)
    print(res)

    coins = [1, 2, 5]
    amount = 11
    res = so.coinChange(coins,amount)
    print(res)

    coins = [1]
    amount = 0
    res = so.coinChange(coins,amount)
    print(res)

    coins = [1]
    amount = 1
    res = so.coinChange(coins,amount)
    print(res)