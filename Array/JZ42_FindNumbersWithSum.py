# -*- coding:utf-8 -*-
'''
双指针
题目是递增数列，所以可以使用双指针，当两边之和小于sum时，左指针右移增大；
当两边之和大于sum时，右指针左移减小，时间复杂度o(n)，这样不用全部遍历一遍（o(n2))，体现出在单调序列
中双指针的好处。
另一方面，结合数学知识，当a,b>0时，a+b >2*sqrt(ab)，
所以第一次满足要求的就可以直接输出了，在有负数的情况下依然成立！！！
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 1:
            return []

        left = 0
        right = len(array)-1

        while left < right:
            tmp = array[left] + array[right]
            if tmp == tsum:
                return [array[left],array[right]]
            elif tmp < tsum:
                left += 1
            else:
                right -= 1
        return []


if __name__ == '__main__':
    func = Solution()
    array = [1,2,3,4,5,6]
    tsum = 7
    print(func.FindNumbersWithSum(array,tsum))



