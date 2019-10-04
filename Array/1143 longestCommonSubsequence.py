class Solution:
    def longestCommonSubsequence(self, text1, text2):
        size1 = len(text1)
        size2 = len(text2)
        if not size1 or not size2:
            return 0

        dp = [[0]*(size2+1) for _ in range(size1+1)]
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
    print(so.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(so.longestCommonSubsequence(text1 = "abc", text2 = "def"))
