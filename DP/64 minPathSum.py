class Solution:
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


if __name__ == '__main__':
    so = Solution()
    a = [[1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]]
    res = so.minPathSum(a)
    print(res)



