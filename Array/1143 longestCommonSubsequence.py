class Solution1:
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

'''
2020/12/3 18:32
方法一 动态规划
dp[i][j]:text1的前i个元素和text2的前j个元素的最长公共子序列
然后依次“填表”。
注意其中当两者不想等时的比较对象 dp[i][j] = max(dp[i-1][j],dp[i][j-1])

'''
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0]*(1+n2) for _ in range(1+n1)]
        for i in range(1,1+n1):
            for j in range(1,1+n2):
                if text1[i - 1] == text2[j -1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 这里可以不用比较dp[i-1][j-1]，因为两个字符串都缩短了，
                    # 其结果不会大于只缩短其中一个字符的结果
                    # dp[i][j] = max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]



if __name__ == '__main__':
    so = Solution()
    print(so.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
    print(so.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(so.longestCommonSubsequence(text1 = "abc", text2 = "def"))
