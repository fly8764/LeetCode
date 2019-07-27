class Solution:
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


if __name__ == '__main__':
    so = Solution()
    coins = [2] #[1, 2, 5]
    amount = 3 #3 11
    res = so.coinChange(coins,amount)
    print(res)
