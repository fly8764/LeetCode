'''
一上来第一反应，分类讨论，四种情况；
其实只有计算位置[i][j]不是障碍物，就可以直接计算，像62题那样。
因为如果上面或左面有障碍物，默认dp为0，加上去也无效。
'''
class Solution:
    def uniquePathsWithObstacles3(self, obstacleGrid):
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

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            if not obstacleGrid[0][i]:
                dp[0][i] = 1
            else:
                break

        for j in range(m):
            if not obstacleGrid[j][0]:
                dp[j][0] = 1
            else:
                break

        for i in range(1,m):
            for j in range(1,n):
                '''
                一上来第一反应，分类讨论，四种情况；
                其实只有计算位置[i][j]不是障碍物，就可以直接计算，像62题那样。
                因为如果上面或左面有障碍物，默认dp为0，加上去也无效。
                '''
                # if not obstacleGrid[i-1][j] and not obstacleGrid[i][j-1]:
                #     dp[i][j] = dp[i][j-1] + dp[i-1][j]
                # elif not obstacleGrid[i-1][j] and obstacleGrid[i][j-1]:
                #     dp[i][j] = dp[i-1][j]
                # elif obstacleGrid[i-1][j] and not obstacleGrid[i][j-1]:
                #     dp[i][j] = dp[i - 1][j]
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

class Solution1:
    def uniquePathsWithObstacles(self, grid):
        m = len(grid)
        if m < 1:return 0
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]

        for i in range(n):
            if grid[0][i] == 0:
                dp[0][i] = 1
            else:break

        for i in range(m):
            if grid[i][0] == 0:
                dp[i][0] = 1
            else:break

        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]]
    res = so.uniquePathsWithObstacles(grid) #[[0,0,0],[0,1,0],[0,0,0]] [[1]]
    print(res)
    # grid = [[0,0,0],[0,1,0],[0,0,0]] [[1]]
    # res = so.uniquePathsWithObstacles([[0,0],[1,0]]) #
    # print(res)
