# -*- coding:utf-8 -*-
import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False

    def duplicate(self, numbers, duplication):
        dic = []
        for item in numbers:
            if item not in dic:
                dic.append(item)
            else:
                duplication[0] = item
                return True
        return False
    # def duplicate(self, numbers, duplication):
    #     flag = False
    #     c = collections.Counter(numbers)
    #     for key,value in c.items():
    #         if value > 1:
    #             duplication[0] = key
    #             flag = True
    #             break
    #     return flag


if __name__ == '__main__':
    so = Solution()
    nums = [2,1,3,1,4] #[2,3,1,0,2,5,3]
    n = len(nums)
    res = so.duplicate(n,nums)
    print(res)
