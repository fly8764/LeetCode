class Solution2:
    def change(self, amount, coins):
        size = len(coins)
        dp = [0]*(amount+1)
        #dp[0] :不用硬币即可
        dp[0] =1
        #要把 coins的循环放在 外层循环，因为 使用一个coin，dp要往前回溯
        #如果把amount放在外层，每次i增加，都要重新寻找满足i要求的硬币组合数，没有起到利用
        #子结构的效果
        for item in coins:
            for i in range(1,amount+1):
                if i >= item:
                    dp[i] += dp[i-item]
        return dp[-1]

class Solution1:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[1] + [0] * amount for _ in range(len(coins) + 1)]
        # print(dp)
        n = len(coins)
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        # print(dp)
        return dp[-1][-1]
'''
2020/12/1 0:09
完全背包问题，计数型，不是求最值型
1.优化空间后的一维数组，顺序计算。
2.两种for循环方式

'''
class Solution:
    def change(self, amount, coins):
        n = len(coins)

        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(n):
            for j in range(coins[i],amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[-1]

if __name__ == '__main__':
    so = Solution()
    res = so.change(5,[1, 2, 5])
    print(res)


