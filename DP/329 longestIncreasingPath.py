'''
常规的dfs题，暴力法求解，可以过，对每个点都遍历一次
self.vis[i][j]代表(i,j)为起点的路径的最长上升序列的长度
每次递归，都是沿着上升序列进行扩展 搜索，默认遍历的情况下，
在一个点(i,j)在搜索上升序列的过程中，从最高点，出栈时，会依次
把各个点的最长路径长度，标记下来；所以，不用担心考虑，高于点(i,j)
点的值的最长路径长度是否正确。
'''
class Solution:
    def dfs(self,x,y):
        if self.vis[x][y] > 0:
            return self.vis[x][y]
        ans = 0
        for item in self.dir:
            x_n = x + item[0]
            y_n = y + item[1]
            if 0<= x_n < self.row and 0<= y_n < self.col and self.matrix[x][y] < self.matrix[x_n][y_n]:
                ans = max(ans,self.dfs(x_n,y_n))
        self.vis[x][y] = ans + 1
        return self.vis[x][y]

    def longestIncreasingPath(self, matrix):
        self.row = len(matrix)
        if self.row < 1:return 0
        self.col = len(matrix[0])
        self.vis = [ [0]*self.col for _ in range(self.row)]
        res = 0
        self.dir = [[0,1],[0,-1],[1,0],[-1,0]]
        self.matrix = matrix
        for i in range(self.row):
            for j in range(self.col):
                res = max(res,self.dfs(i,j))
        return res

class Solution1:
    #非递归法，动态规划
    pass


if __name__ == '__main__':
    so = Solution()
    matrix = [
  [9,9,4],
  [6,6,8],
  [2,1,1]]
    res = so.longestIncreasingPath(matrix)
    print(res)
    matrix = [
  [3,4,5],
  [3,2,6],
  [2,2,1]]
    res = so.longestIncreasingPath(matrix)
    print(res)

    matrix = [[0],[1],[5],[5]]
    res = so.longestIncreasingPath(matrix)
    print(res)
