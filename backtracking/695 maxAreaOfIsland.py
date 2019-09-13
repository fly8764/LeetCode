class Solution():
    def __init__(self):
        pass

    def inarea(self,i,j):
        if 0<= i and i< self.m and j >= 0 and  j < self.n:
            return True
        else:
            return False

    def dfs(self,i,j):
        self.cnt += 1
        self.marked[i][j] = 1
        for item in self.dir:
            x = i + item[0]
            y = j + item[1]
            if self.inarea(x,y) and not self.marked[x][y] and self.grid[x][y]:
                self.dfs(x,y)

    def maxAreaOfIsland(self,grid):
        self.grid = grid
        self.m = len(grid)
        if self.m < 1:
            return 0
        self.n = len(grid[0])
        if self.n < 1:
            return 0

        self.marked = [[0]*self.n for _ in range(self.m)]

        self.dir = [[0,-1],[0,1],[-1,0],[1,0]]

        max_ = 0
        for i in range(self.m):
            for j in range(self.n):
                if not self.marked[i][j] and grid[i][j]:
                    self.cnt = 0
                    self.dfs(i,j)
                    max_ = max(max_,self.cnt)

        return max_

