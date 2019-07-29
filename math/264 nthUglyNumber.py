class Solution:
    #方法一：遍历从1开始的数字，每次加1，并对每个数字判断是否为丑数；超时
    #二：使用动态规划，每次对之前的三个数中，分别乘以2，3，5，然后找到最小，
    # 放入栈中(避免跨步大，漏掉值)
    #为了避免重复计算，使用if结构，而不是if else，来对相同的值更新下标

    def nthUglyNumber(self, n):
        if n < 1:
            return False
        dp = [0]*n
        dp[0] = 1
        id2 = id3 = id5 = 0
        for i in range(1,n):
            min_ = min(dp[id2]*2,dp[id3]*3,dp[id5]*5)
            if min_ == dp[id2]*2:
                id2 += 1
            if min_ == dp[id3]*3:
                id3 += 1
            if min_ == dp[id5]*5:
                id5 += 1
            dp[i] = min_
        return dp[-1]

    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return False
        dp = [0] * index
        dp[0] = 1
        id2 = id3 = id5 = 0
        for i in range(1, index):
            min_ = min(dp[id2] * 2, dp[id3] * 3, dp[id5] * 5)
            if min_ == dp[id2] * 2:
                id2 += 1
            if min_ == dp[id3] * 3:
                id3 += 1
            if min_ == dp[id5] * 5:
                id5 += 1
            dp[i] = min_
        return dp[-1]



    def isUgly(self, num):
        #1是丑数；特例
        if num < 1:
            return False
        while num != 1:
            if num % 2 == 0:
                num /= 2
                continue
            if num % 3 == 0:
                num /= 3
                continue
            if num % 5 == 0:
                num /= 5
                continue
            return False
        return True


if __name__ == '__main__':
    so = Solution()
    res = so.nthUglyNumber(253)
    print(res)
    res = so.GetUglyNumber_Solution(253)
    print(res)


