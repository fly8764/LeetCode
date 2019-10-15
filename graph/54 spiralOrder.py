'''
按照定义，不断地在四周循环，每遍历完一条边界，都要更改边界值，即边界范围
'''
class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if not m:return []
        n = len(matrix[0])
        res = []
        up,down = 0,m-1
        left,right = 0,n-1
        #一直沿着四周的边界走，所以要不断地改变边界值
        while True:
            #遍历上边界
            for i in range(left,right+1):
                res.append(matrix[up][i])
            #修改上边界
            up += 1
            #上边界不能超过下边界，否则推出循环
            if up > down:break
            #修改后的上边界，直接作为往下遍历的其实值,

            # 遍历右边界
            for i in range(up,down+1):
                res.append(matrix[i][right])
            # 修改右边界
            right -= 1
            if right < left:break

            #遍历下边界
            for i in range(right,left-1,-1):
                res.append(matrix[down][i])
            #修改下边界
            down -= 1
            if down < up:break

            #遍历左边界,上升
            for i in range(down,up-1,-1):
                res.append(matrix[i][left])
            #修改左边界
            left += 1
            if left > right:break
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))