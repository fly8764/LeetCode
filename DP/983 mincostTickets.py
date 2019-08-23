#典型的动态规划题目，
#空间换时间，为了减少 循环找到 最左边的  7天，30天，使用一个396的列表，
#这种方法 当days大时，估计比较快
class Solution:
    def mincostTickets(self, days, costs):
        size = len(days)
        dp = [0]*(days[-1] + 31)
        dayset = set(days)
        for i in range(1,len(dp)):
            if i not in dayset:
                dp[i] += dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0],dp[i-7]+costs[1],dp[i-30]+costs[2])
        return dp[-1]

    # def mincostTickets(self, days, costs):
    #     size = len(days)
    #     dp = [0]*(366+30) #防止 计算前30天时 dp[i-30] i-30 < 0 在前面加了 30个空位
    #     idx = 0
    #     i = 31
    #     while i < 396 and idx < size:
    #         if (days[idx] + 30) != i:
    #             dp[i] = dp[i-1] # 把当前的计算结果往后扩充，直至下一个旅游天的出现
    #             i += 1 # 别忘了加1
    #             continue
    #         #计算新的一个旅游天的最低费用
    #         dp[i] = min(dp[i-1]+costs[0],dp[i-7]+costs[1],dp[i-30]+costs[2])
    #         idx += 1
    #         i += 1 # 别忘了加1
    #     return dp[days[-1]+ 30]

if __name__ == '__main__':
    so = Solution()
    # days = [1,4,6,7,8,20]
    # days = [1,2,3,4,5,6,7,8,9,10,30,31]
    days = [1,4,6,7,8,365]
    costs = [2,7,15]

    res = so.mincostTickets(days,costs)
    print(res)


