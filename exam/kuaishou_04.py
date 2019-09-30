class Solution():
    def check(self,grid,x,y,d):
        dic = {}
        for i in range(x,x+d):
            for j in range(y,y+d):
                if '0'<= grid[i][j]<= '9':
                    if grid[j][i] not in dic:
                        dic[grid[j][i]] = 1
                    else:return False
        return True


    def find(self,grid):
        #判断行
        for i in range(9):
            dic = {}
            for j in range(9):
                if '0'<=grid[i][j]<= '9':
                    if grid[i][j] not in dic:
                        dic[grid[i][j]] = 1
                    else:return False
        #判读lie
        for i in range(9):
            dic = {}
            for j in range(9):
                if '0'<=grid[j][i]<= '9':
                    if grid[j][i] not in dic:
                        dic[grid[j][i]] = 1
                    else:return False
        #判断块
        for x in [0,3,6]:
            for y in [0,3,6]:
                res = self.check(grid,x,y,3)
                if not res:
                    return False

        return True


if __name__ == '__main__':
    so = Solution()

    grid = []
    for i in range(9):
        grid.append(input())
    # print(grid)

    res = so.find(grid)
    if res:
        print('true')
    else:
        print('false')
# 53XX7XXXX
# 6XX195XXX
# X98XXXX6X
# 8XXX6XXX3
# 4XX8X3XX1
# 7XXX2XXX6
# X6XXXX28X
# XXX419XX5
# XXXX8XX79