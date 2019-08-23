class Solution:
    # S:j  T:i
    #dp[i][j] 代表 S的前j个字符串中可以构成 T的前i个字符串的个数
    #S[j] == T[i]时，dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    #字符S[j]可参与 dp[i-1][j-1]，可不参与(其前j-1个字符串能构成T[:i]的个数) dp[i][j-1]
    #S[j] != T[i]时，dp[i][j] = dp[i][j-1],看 S[:j-1]能构成的个数
    def numDistinct(self, s, t):
        dp = [[1]*(len(s)+1) for _ in range(len(t)+1)]
        for i in range(1,len(t)+1):
            dp[i][0] = 0
            for j in range(1,len(s)+1):
                if s[j-1] == t[i-1]:
                    # 相比于下面一个，多了dp[i-1][j-1]，即s[j]参与构造
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    so = Solution()
    s = "rabbbit"
    t = "rabbit"
    res = so.numDistinct(s,t)
    print(res)
