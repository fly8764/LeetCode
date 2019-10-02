'''
动态规划，从低到上，逐层地实现，根据已得到的结论，来推断下一个
S:j  T:i
dp[i][j] 代表 S的前j个字符串中可以构成 T的前i个字符串的子序列个数
S[j] == T[i]时，dp[i][j] = dp[i-1][j-1] + dp[i][j-1]，数量上增加
字符S[j]可参与（即使用s[j]作为匹配的一部分,跟在前面已经匹配的字符的后面） dp[i-1][j-1]，
可不参与（即不使用s[j],使用上一个可以匹配的字符,以往的匹配好的个数，形式上是s[j-1],其实s[j-1]可能是更前面的位置传过来的，
(其前j-1个字符串能构成T[:i]的个数) dp[i][j-1]
S[j] != T[i]时，dp[i][j] = dp[i][j-1],看 S[:j-1]能构成的个数,数量不增加，是一种传递
这里的分类讨论是在不同情况下的处理方法，不是同一情况
'''
class Solution:
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

class Solution1:
    def numDistinct(self, s, t):
        size1 = len(s)
        size2 = len(t)
        dp = [[0]*(size1+1) for _ in range(size2+1)]
        dp[0] = [1]*(size1+1)
        for i in range(1,size2+1):
            for j in range(1,size1+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution1()
    s = "rabbbit"
    t = "rabbit"
    res = so.numDistinct(s,t)
    print(res)
