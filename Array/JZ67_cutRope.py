# -*- coding:utf-8 -*-
'''
动态规划
f[i]:长度为i的绳子的最大结果
绳子至少要裁剪一次，所以f[i] = max{f[i],j*f[i-j]} (0<j<j)
对于每个长度i找到该情况下的最大结果，一直计算，最后得到最终的结果。
有特殊情况 i=2时，result= 1；i=3，result=2；i=4，result=4；
'''
class Solution:
    def cutRope(self, number):
        if number == 2:return 1
        if number == 3:return 2

        f = [1,2,3,4]+[1]*(number-4)
        for i in range(4,number):
            for j in range(1,i):
                f[i] = max(f[i],j*f[i-j])
        return f[-1]

if __name__ == '__main__':
    func = Solution()
    print(func.cutRope(10))

