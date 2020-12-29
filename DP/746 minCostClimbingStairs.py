class Solution1:
    def minCostClimbingStairs(self,cost):
        length = len(cost)
        if length == 0:
            return 0
        if length == 1:
            return cost[0]

        if length == 2:
            return min(cost[0],cost[1])

        dp = [0 for _ in range(length+1)]
        dp[0] = dp[1] = 0

        for i in range(2,length+1):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2]+cost[i-2])

        return dp[length]

'''
第二次做这个题目，一直过不了，题意理解不对。
正确做法：
dp[i]：到达第i层消耗的体力，如果不跨过该层，则不消耗该层的体力cost[i]。
因此，dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
题目要求到达顶层，因此要跨过最后一个梯子，即求dp[n+1]。

错误做法：
到达第i层，可以是i-2层跨两步，消耗cost[i]，或者第i-1层跨两步，不消耗额外体力,因为两步跨过去了。
这就有错误，一方面，定义不一致，i-2跨两步，正好到达第i层，i-1跨两步，跨过了第i层,那到达了第i+1层，应该消耗cost[i+1]啊！这里没有体现出来；
另一方面，始终没有跨一步，这就有问题。
所以定义出现问题，后面很可能出问题。
dp[i] = min(dp[i-2]+cost[i],dp[i-1])
看来dp[i]的定义确实有问题。
'''
class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 2:return min(cost)

        dp = [1000]*(n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            dp[i] =  min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[-1]




if __name__ == '__main__':
    so = Solution()
    # cost = [10,15,20]
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost = [0,0,1,0]
    res = so.minCostClimbingStairs(cost)
    print(res)