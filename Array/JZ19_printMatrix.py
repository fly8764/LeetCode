'''
顺时针打印二维数组，其中一个重要的技巧是 “左转90°”，其方法是
从右往左，把每一列转变成一行
这个有很强的技巧性！！！
'''
class Solution:
    def turn(self,matrix):
        row = len(matrix)
        col = len(matrix[0])
        A = []
        for i in range(col-1,-1,-1):
            B = []
            for j in range(row):
                B.append(matrix[j][i])
            A.append(B)
        return A

    def printMatrix(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                break

            matrix = self.turn(matrix)
        return result


