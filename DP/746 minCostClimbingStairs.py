class solution:
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

if __name__ == '__main__':
    so = solution()
    res = so.minCostClimbingStairs([10,15,20])
    print(res)