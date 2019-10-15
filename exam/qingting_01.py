class Solution:
    def find(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0 : return []
        lenX = len(matrix[0])
        lenY = len(matrix)
        startX = 0
        endX = lenX
        startY = 0
        endY = lenY
        l = []
        while (startX <= endX and startY <= endY):
            if (startY<endY):
                for i in range(startX,endX):
                    l.append(matrix[startY][i])
            startY+=1
            if (startX<endX):
                for i in range(startY,endY):
                    l.append(matrix[i][endX-1])
            endX-=1
            if (startY<endY):
                for i in range(startX,endX)[::-1]:
                    l.append(matrix[endY-1][i])
            endY-=1
            if (startX<endX):
                for i in range(startY,endY)[::-1]:
                    l.append(matrix[i][startX])
            startX+=1
        return l


if __name__ == '__main__':
    so = Solution()
    print(so.find([[1,2,3],[4,5,6],[7,8,9]]))