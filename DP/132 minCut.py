#典型的动态规划，找到各个子问题的最优解，
#dp[i]: 从起始到位置i的子串的最小分割数；
#对应新的字符串 j，当 i+1:j的部分子串 为回文串时，其可作为一种分割方式，分割数为 dp[i]+1,
#转移方程为 dp[i] = min(dp[i],dp[j-1]+1)
class Solution:
    def minCut(self, s):
        size = len(s)
        if not size or s[::]==s[::-1]:
            return 0

        dp = [float('inf')]*(size )

        for i in range(size):
            for j in range(i+1):
                #为了保证取到 s[i:i+1],即以子串的“最后一个字符”为单个字符的情况，包括只有一个字符的情况
                sub = s[j:i+1]
                if j == 0 and sub[::] == sub[::-1]:
                    dp[i] = 0
                elif sub[::] == sub[::-1]:
                    dp[i] = min(dp[i],dp[j-1]+1)
        return dp[-1]

if __name__ == '__main__':
    so = Solution()
    s = 'aab'
    res = so.minCut(s)
    print(res)



