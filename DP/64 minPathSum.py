class Solution2:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        for i in range(1,n):
            grid[0][i] = grid[0][i] + grid[0][i-1]
        for j in range(1,m):
            grid[j][0] = grid[j][0] + grid[j-1][0]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]

        return grid[-1][-1]

class Solution1:
    def minPathSum(self, grid):
        m = len(grid)
        if m < 1:return
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = grid[i][0]+dp[i-1][0]
        for i in range(1,n):
            dp[0][i] = grid[0][i] +dp[0][i-1]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]

class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = grid[0]
        for i in range(1,n):
            dp[i] = dp[i-1] + grid[0][i]
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][0]
                else:
                    dp[j] = min(dp[j-1],dp[j]) + grid[i][j]
        return dp[-1]




if __name__ == '__main__':
    so = Solution1()
    # a = [[1, 3, 1],
    #      [1, 5, 1],
    #      [4, 2, 1]]
    a = [[1,2,3],[4,5,6]]
    res = so.minPathSum(a)
    print(res)



