# -*- coding:utf-8 -*-
'''
重点(这个题目的关键细节)：
把一个大问题拆成小问题，看其中的重要点。
两个数a,b,定义一种比较规则，如果a+b<b+a，则把a放在b前面；
使用冒泡法，进行一次重排，最后的结果拼接起来即可。
'''
# class Solution:
#     def compare(self,a,b):
#         tmp1 = int(str(a)+str(b))
#         tmp2 = int(str(b)+str(a))
#         if tmp1 > tmp2:
#             return True
#         else:
#             return False
#
#     def PrintMinNumber(self, numbers):
#         n = len(numbers)
#         if n < 1:return None
#         if n < 2:return numbers[0]
#         # 冒泡法
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if self.compare(numbers[i],numbers[j]):
#                     tmp = numbers[i]
#                     numbers[i] = numbers[j]
#                     numbers[j] = tmp
#         result = list(map(lambda x:str(x),numbers))
#         return int(''.join(result))

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
        # 注意这种边界情况，即空表的！！！
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
    func = Solution()
    numbers = [3,32,321]
    result = func.PrintMinNumber(numbers)
    print(type(result))