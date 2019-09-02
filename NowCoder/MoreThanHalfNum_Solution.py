# -*- coding:utf-8 -*-
#19:55 --  20:10
class Solution:
    def MoreThanHalfNum_Solution(self, nums):
        if not nums:return 0
        size = len(nums)
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            #对应长度为1的考虑，这个判断条件不能写在else里面，
            if dic[i] > (size // 2):
                return i

        return 0

if __name__ == '__main__':
    so = Solution()
    nums = [1,2,3,2,2,2,5,4,2]
    res = so.MoreThanHalfNum_Solution(nums)
    print(res)