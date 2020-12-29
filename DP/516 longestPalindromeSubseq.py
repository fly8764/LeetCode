#encoding: utf-8
class Solution1:

    def longestPalindromeSubseq(self,s):
        length = len(s)
        if length == 0:
            return 0

        dp = [[0 for _ in range(length)] for _ in range(length)]
        # dp[length-1][length-1] = 1

        # for r in range(length):
        for r in range(length):
            dp[r][r] = 1
            # for l in range(r):
            for l in range(r-1,-1,-1):
                # 因为这里是 回文子序列，不要求是连续子串，所以，下面的判断条件不同
                #右边界确定后，左边逐渐往左去，而不是直接从0往右去，
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l+1][r],dp[l][r-1])

        return dp[0][length-1]

'''
2020/12/3 22:04 
动态规划  子序列而不是字串 注意了
这里虽然是一个字符串，但是需要用到二维数组来遍历；同时是否是回文串，需要用到中间的内容，所以
需要注意左指针的移动方向，从右往左移动。
也要注意 对角线的值需要提前填充，因为对角线附近的dp计算需要用到。
'''
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        if n < 2:return n

        dp = [[0]*n for _ in range(n)]
        for r in range(n):
            # 这里需要把对角线的值填上，因为对角线附近的dp可能用到
            # 另一方面，右边界不需要从1开始，即使从0开始，下面也不会进入循环
            dp[r][r] = 1
            for l in range(r-1,-1,-1):
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l+1][r],dp[l][r-1])

        return dp[0][n-1]




if __name__ == '__main__':
    so = Solution()
    res = so.longestPalindromeSubseq("cbbd")
    print(res)