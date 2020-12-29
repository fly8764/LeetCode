
class Solution1:
    def  __init__(self):
        self.result = []
        self.num = 0
        self.cur = []
        self.vis = []
        self.ans = 0


    def output(self):
        tmp_result = []
        for i in range(self.num):
            line = ""
            for j in range(self.num):
                # self.cur[i]代表第i层Q放置位置（列）
                if j == self.cur[i]:
                    line += "Q"
                else:
                    line += "."
            tmp_result.append(line)
        self.result.append(tmp_result)

    def solve(self,row):
        if row == self.num:
            self.ans += 1
            # print(self.cur)
            self.output()
        else:
            '''
            正对角线：y=x即 i=row+b,->-b = row-i,（-(num-1) <= b <= (num-1)）由于数组中没有负索引，所以两边同时加num,
            即 num-b = row-i+num，值域[0,2*num-1]
            副对角线：y=b-x,即row+i= b （0<=b<=2*num-1）
            不同的对角线对应不同的b，因此可以把b当作状态数组的下标，来判断该对角线是否有值，对应的位置是否可以放置。
            根据状态方程的取值个数，可以选择一个大小为2*num的数组。
            第二次做该题时，被正对角线的表达方式 row-i+num 困扰了很近，其是为了避免负索引的。
            '''

            for i in range(self.num):
                if not self.vis[0][i] and not self.vis[1][row+i] and not \
                        self.vis[2][row-i+self.num]:
                    self.cur[row] = i
                    self.vis[0][i] = self.vis[1][row+i] = self.vis[2][row-i+self.num] = 1
                    self.solve(row+1)
                    self.vis[0][i] = self.vis[1][row + i] = self.vis[2][row - i + self.num] = 0

    def solveNQueens(self,n):
        self.num = n
        self.cur = [0]*n
        for i in range(3):
            self.vis.append([0]*n*2)
        self.solve(0)

        return  self.result

class Solution:
    def output(self):
        tmp = []
        for i in range(self.n):
            # line = '.'*self.n
            # # self.cur[i]第i行皇后的放置位置
            # str类型不支持索引
            # line[self.cur[i]] = 'Q'
            line = ''
            for j in range(self.n):
                if self.cur[i] == j:
                    line += 'Q'
                else:
                    line += '.'
            tmp.append(line)
        self.res.append(tmp)


    def solver(self,row):
        if row == self.n:
            self.ans += 1
            self.output()
        else:
            for i in range(self.n):
                if not self.vis[0][i] and not self.vis[1][row + i] and not self.vis[2][row - i + self.n]:
                    # 占领位置，同时把列和两个对角线也占领。
                    self.cur[row] = i
                    self.vis[0][i] = self.vis[1][row + i] = self.vis[2][row - i + self.n] = 1
                    self.solver(row + 1)
                    # 换个位置，把刚才占领的列和对角线撤销
                    self.vis[0][i] = self.vis[1][row + i] = self.vis[2][row - i + self.n] = 0


    def solveNQueens(self, n):
        # self.cur数组中每个值cur[i]表示第i行皇后的放置位置
        self.cur = [0]*n
        self.res = []
        self.ans = 0
        self.n = n
        self.vis = []
        '''
        1.vis = [[0]*2*n]*3
        2.下面的for循环
        第一种是“行复制”，如果vis[0][0] = 1,则下面所有行的第一列均会变化，为1;
        各行之间是复制关系，任意一行变了，其它行都变，所以这种方法慎用。
        '''

        for i in range(3):
            self.vis.append([0]*2*n)

        self.solver(0)

        return self.res


if __name__ == '__main__':
    func = Solution()
    n = 4
    print(func.solveNQueens(n))
