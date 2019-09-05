# -*- coding:utf-8 -*-
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。

思路：m，n  如果拼接后的数mn < nm 则认为 m小于n，m应排在 n 前面，
按照这种排序方法，来排序，最终的得到结果；
证明：通过反证法

输出要求是字符串

很考察 数学能力…………
T(n) = nlogn 即排序的时间复杂度
'''
# 20:57--
import functools


class Solution:
    def cmp(self,a,b):
        if a+b < b + a:
            return -1
        elif a + b > b + a:
            return 1
        else:
            return 0

    def PrintMinNumber(self, numbers):
        if not numbers:return ''

        res = []
        for item in numbers:
            res.append(str(item))

        #自定义排序函数
        ans = sorted(res,key=functools.cmp_to_key(self.cmp))
        # ans = list(map(int,ans))
        temp = ''
        for item in ans:
            temp += item
        return temp

if __name__ == '__main__':
    so = Solution()
    nums = [3,32,321]
    res = so.PrintMinNumber(nums)
    print(res)
    # def cmp(a,b):
    #     if a+b < b + a:
    #         return -1
    #     elif a + b > b + a:
    #         return 1
    #     else:
    #         return 0

    # size = len(nums)
    # res = []
    # for item in nums:
    #     res.append(str(item))
    #
    # ans = sorted(res, key=functools.cmp_to_key(cmp))
    # ans = list(map(int,ans))
    # print(ans)
