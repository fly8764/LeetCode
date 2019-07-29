class Solution:
    def maximalRectangle(self, matrix):
        # 每个点的最大高度
        # if not matrix: return 0
        row = len(matrix)
        if not row:
            return 0
        col = len(matrix[0])

        left = [0] * col
        right = [col] * col #这里的初始化要注意
        hight = [0] * col

        max_area = 0

        for i in range(row):
            cur_left, cur_right = 0, col
            for j in range(col):
                #把两个大致相同的for循环放在一起，并不会节约多少时间
                if matrix[i][j] == '1':
                    hight[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    hight[j] = 0
                    left[j] = 0
                    cur_left = j + 1

            # for j in range(col):
            #     if matrix[i][j] == '1':
            #         left[j] = max(left[j], cur_left)
            #     else:
            #         # 这里当 matrix[i][j] == '0'时，令left[j] = 0 是为了在下一次迭代时
            #         # 在max函数中，0的影响最小；不用担心 下面 right- left 导致宽度增加，
            #         # 因为有 hight[j] = 0 在，这一点的扩展的最大面积为 0
            #         left[j] = 0
            #         cur_left = j + 1

            for j in range(col - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = col
                    cur_right = j
            for j in range(col):
                max_area = max(max_area, hight[j] * (right[j] - left[j]))

        return max_area

    def maximalRectangle01(self, matrix):
        #超时
        #下面的dp构造方式 和 dp = [[0]*col]*row 导致运行结果不一样，简单的相乘，错误
        #通过动态规划 每行，求取以每个点为右下角端点时的最大宽度，
        #高度，直接i-k+1,网上逐层遍历，当中间有0 出现时，其width 为0，width的选取使用min()，因此不用
        # 担心中间断层的影响，从下往上，断层之上的width，area都为0
        if not matrix: return  0
        row = len(matrix)
        col = len(matrix[0])
        # dp = [[0]*col]*row
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        max_area = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0': continue
                #j = 0,因为matrix[i][j] == '1'，所以 赋值width = dp[i][j] = 1
                width = dp[i][j] = dp[i][j-1] +1 if j else 1

                for k in range(i,-1,-1):
                    width = min(width,dp[k][j])
                    max_area = max(max_area,width*(i-k+1))

        return max_area

    def maximalRectangle0(self, matrix):
        #直接使用221中的求 左 上 左上角 三个地方的最小值加1，这种方法行不通 超时
        row = len(matrix)
        col = 0
        if row:
            col = len(matrix[0])
        if not row or not col:
            return 0

        max_w = max_h = 0
        pre_w = pre_h = 0
        dp_w = [0] *(col+1)
        dp_h = [0] *(col+1)

        for i in range(1,row+1):
            for j in range(1,col+1):
                temp_w = dp_w[j]
                temp_h = dp_h[j]
                if matrix[i-1][j-1] == '1':
                    dp_w[j] = min(dp_w[j-1],dp_w[j],pre_w)+1
                    max_w = max(dp_w[j],max_w)
                    dp_h[j] = min(dp_h[j-1],dp_h[j],pre_h)+1
                    max_h = max(dp_h[j],max_h)
                else:
                    dp_w[j] = 0
                    dp_h[j] = 0
                pre_w = temp_w
                pre_h = temp_h
        return max_w * max_h

if __name__ == '__main__':
    so = Solution()
    matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
    matrix1 = [["1"]]
    matrix2 = [["1","0"]]
    matrix3 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    res = so.maximalRectangle(matrix)
    print(res)

    res = so.maximalRectangle(matrix1)
    print(res)

    res = so.maximalRectangle(matrix2)
    print(res)

    res = so.maximalRectangle(matrix3)
    print(res)




