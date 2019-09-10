'''
思路：
使用回溯法，在四个方向上进行循环遍历，
当确定一个点满足要求时，先占据这个点(对应的marked数组值为1)，然后在四个方向上搜索；
当四个方向 都不满足要求时，退出这个点，清空占位
'''
class Solution:
    def find(self,x,y,k):
        #x,y代表 board的位置，k代表word中的位置，要判断是否配对，配对了再接着往下配对，
        #marked代表 已使用过的位置
        if k == self.k -1:
            return self.board[x][y] == self.word[k]
        if self.board[x][y] == self.word[k]:
            #先占据这个位置，当不成功时，后面再撤掉
            self.marked[x][y] = 1
            for item in self.dir:
                x_new = x + item[0]
                y_new = y + item[1]
                if 0 <= x_new < self.m and 0 <= y_new <self.n and \
                    not self.marked[x_new][y_new] and self.find(x_new,y_new,k+1):
                    return True

            #在不成功时，释放掉位置占位
            self.marked[x][y] = 0
        return False

    def exist(self, board, word):
        self.board = board
        self.m = len(board)
        if self.m == 0:
            return False

        self.n = len(board[0])

        self.word = word
        self.k = len(word)
        self.marked = [[0]*self.n for _ in range(self.m)]
        self.dir = [[-1,0],[1,0],[0,1],[0,-1]]

        for i in range(self.m):
            for j in range(self.n):
                if self.find(i,j,0):
                    return True

        return False

    def dfs(self,i,j,k):
        #这种写法 难以释放 没有成功的位置的占位
        #回溯法：就是要在不满足条件时，回去重新换一个方向；

        #i,j代表board[i][j] == word[k-1],已经匹配好的点
        #k代表要去配对的字符下标
        #要保证不能往回返回

        if k == self.k:
            return True

        left_,right_,up_,down_ = False,False,False,False
        if j > 0:
            # flag = self.flag[i][j-1] #用过 则flag == 1
            left = self.board[i][j - 1] == self.word[k] and not self.marked[i][j-1]
            if left:
                self.marked[i][j - 1] = 1
                left_ =  self.dfs(i, j - 1, k+1)

        if j < self.n - 1:
            right = self.board[i][j + 1] == self.word[k] and not self.marked[i][j+1]
            if right:
                self.marked[i][j + 1] = 1
                right_ = self.dfs(i, j + 1, k + 1)

        if i < self.m - 1:
            down = self.board[i + 1][j] == self.word[k] and not self.marked[i+1][j]
            if down:
                self.marked[i+1][j] = 1
                down_ = self.dfs(i + 1, j, k+1)

        if i > 0:
            up = self.board[i - 1][j] == self.word[k] and not self.marked[i-1][j]
            if up:
                self.marked[i-1][j] = 1
                up_ = self.dfs(i - 1, j, k+1)

        # return sum([left_, right_, up_ , down_]) == 1
        return left_ or right_ or up_ or down_



if __name__ == '__main__':
    so = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']]
    word = 'ABCCED' #SEE ABCB
    print(so.exist(board,'ABCCED'))
    print(so.exist(board,'SEE'))
    print(so.exist(board,'ABCB'))


