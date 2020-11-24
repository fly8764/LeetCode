# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        column = len(array[0])

        i = row-1
        j = 0
        while i >=0 and j <=column-1:
            tmp = array[i][j]
            if tmp == target:
                return True
            elif tmp < target:
                j += 1
            else:
                i -= 1
        return False


if __name__ == '__main__':
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    target = 100

    func = Solution()
    print(func.Find(target,array))

