# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def findFirst(self,num):
        cnt = 0
        while num &1 == 0:
            num >>= 1
            cnt += 1
        return cnt
    def isTrue(self,num,cnt):
        num = num>>cnt
        return num & 1

    # def FindNumsAppearOnce(self, array):
    #     size = len(array)
    #     if size < 3:return array
    #     res = []
    #     dic = {}
    #     for item in array:
    #         if item not in dic:
    #             dic[item] = 1
    #         else:
    #             dic[item] += 1
    #     for key,value in dic.items():
    #         if value == 1:
    #             res.append(key)
    #     return res

    def FindNumsAppearOnce(self, array):
        #异或解法
        size = len(array)
        if size < 2:return
        temp = 0
        for item in array:
            temp ^= item
        cnt = self.findFirst(temp)

        num1,num2 = 0,0
        for item in array:
            if self.isTrue(item,cnt):
                num1 ^= item
            else:
                num2 ^= item
        return [num1,num2]






if __name__ == '__main__':
    so = Solution()
    nums = [1,1,2,2,3,4]
    res = so.FindNumsAppearOnce(nums)
    print(res)