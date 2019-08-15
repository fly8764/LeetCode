#encoding: utf-8
class Solution:

    def longestPalindromeSubseq(self,s):
        pass

    # def longestPalindromeSubseq(self,s):
    #     length = len(s)
    #     if length == 0:
    #         return 0
    #
    #     dp = [[0 for _ in range(length)] for _ in range(length)]
    #     # dp[length-1][length-1] = 1
    #
    #     # for r in range(length):
    #     for r in range(length):
    #         dp[r][r] = 1
    #         # for l in range(r):
    #         for l in range(r-1,-1,-1):
    #             #右边界确定后，左边逐渐往左去，而不是直接从0往右去，
    #             if s[l] == s[r]:
    #                 dp[l][r] = dp[l+1][r-1] + 2
    #             else:
    #                 dp[l][r] = max(dp[l+1][r],dp[l][r-1])
    #
    #     return dp[0][length-1]



if __name__ == '__main__':
    so = Solution()
    res = so.longestPalindromeSubseq("cbbd")
    print(res)