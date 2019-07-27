class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,n):
            obstacleGrid[0][i] = int(not obstacleGrid[0][i] and obstacleGrid[0][i-1])
        for j in range(1,m):
            obstacleGrid[j][0]  = int(not obstacleGrid[j][0] and obstacleGrid[j-1][0])

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]

    def uniquePathsWithObstacles2(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n  for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1

        for j in range(m):
            if obstacleGrid[j][0] == 1:
                break
            else:
                dp[j][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[-1][-1]


    def uniquePathsWithObstacles1(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [ [0 for _ in range(n)] for _ in range(m)]

        # dp[0][:] =  1
        # dp[:][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    res = so.uniquePathsWithObstacles([[0,0],[1,0]]) #[[0,0,0],[0,1,0],[0,0,0]] [[1]]
    print(res)
