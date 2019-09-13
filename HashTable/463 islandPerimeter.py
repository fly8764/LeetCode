'''
思路：
原始做法：陆地边界有两种情况，一种是水域；一种是区域的边界
          分情况讨论
方法二：遍历每个节点，对于陆地节点，观察其四个方向的情况，边界或者水域都
直接累加1

方法三：减小一半的计算量，求出上面和左边的边 的个数，最后乘以2；
对于上面， 每条路 都上上面和下面，所以统计出一边的个数，乘以2 即可，
对于左边，是同样的情况。
'''
class Solution:
    def dfs(self,i,j):
        self.marked[i][j] = 1
        for item in self.dir:
            x = i + item[0]
            y = j + item[1]
            if 0 <= x < self.m and 0<= y < self.n:
                if self.grid[x][y]:
                    if not self.marked[x][y]:
                        self.dfs(x, y)
                else: self.cnt += 1
            else:self.cnt += 1

    # def islandPerimeter(self, grid):
    #     self.dir = [[0,1],[0,-1],[1,0],[-1,0]]
    #     self.m = len(grid)
    #     if self.m < 1:
    #         return 0
    #     self.n = len(grid[0])
    #     if self.n < 1:
    #         return 0
    #     self.marked = [[0]*self.n for _ in range(self.m)]
    #     self.grid = grid
    #     self.cnt = 0
    #     flag = 0
    #
    #     for i in range(self.m):
    #         if not flag:
    #             for j in range(self.n):
    #                 if not flag:
    #                     # if grid[i][j] == '1':
    #                     if grid[i][j]:
    #                         self.dfs(i, j)
    #                         flag = 1
    #                 else:
    #                     break
    #         else:
    #             break
    #
    #     return self.cnt

    def islandPerimeter(self, grid):
        self.dir = [[0,1],[0,-1],[1,0],[-1,0]]
        self.m = len(grid)
        if self.m < 1:
            return 0
        self.n = len(grid[0])
        if self.n < 1:
            return 0

        cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]:
                    #左边
                    if j == 0 or grid[i][j-1] ==0:
                        cnt += 1
                    #上面
                    if i == 0 or grid[i-1][j] == 0:
                        cnt += 1
        return cnt *2





if __name__ == '__main__':
    so = Solution()
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    res = so.islandPerimeter(grid)
    print(res)