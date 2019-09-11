'''
'''
#11:00 --
class Solution:
    #如何从孤岛的边界继续遍历下去，寻找下一个孤岛；
    #而不是 从头再来，摒弃已经访问过的孤岛，寻找新的孤岛
    def bfs(self,start_x,start_y):
        #广度优先遍历，寻找邻接点，知道找不到，active为空，岛屿数加1
        active = [[start_x,start_y]]
        while active:
            p = active.pop(0)
            x,y = p[0],p[1]
            # 标记这个点，代表已经走过
            self.marked[x][y] = 1
            #搜集邻域节点
            for item in self.dir:
                x_new = x + item[0]
                y_new = y + item[1]
                #邻域节点为1，且没有被访问过
                if 0 <= x_new < self.m and 0 <= y_new < self.n and \
                        self.grid[x_new][y_new] and not self.marked[x_new][y_new]:
                    active.append([x_new, y_new])
        self.cnt += 1


    def numIslands(self, grid):
        self.cnt = 0
        self.m = len(grid)
        if self.m  < 1:
            return 0
        self.n = len(grid[0])
        self.grid = grid

        self.dir = [[0,1],[0,-1],[-1,0],[1,0]]
        self.marked = [[0]*self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if not self.marked[i][j] and grid[i][j]:
                    self.bfs(i,j)

        return self.cnt


if __name__ == '__main__':
    so = Solution()
    grid = [[1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]]

    grid2 = [[1,1,0,0,0],
             [1,1,0,0,0],
             [0,0,1,0,0],
             [0,0,0,1,1]]
    res = so.numIslands([])
    print(res)



