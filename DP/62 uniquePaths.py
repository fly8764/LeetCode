class Solution1:
    def uniquePaths(self, m: int, n: int):
        cur = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j] += cur[j-1]
        return cur[-1]

class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n
        for i in range(m - 1):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    # res = so.uniquePaths(3,7)
    res = so.uniquePaths(3,2)
    print(res)