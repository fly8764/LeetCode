# -*- coding:utf-8 -*-
'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，
输出两个数的乘积最小的。
21:05 -- 21:17

思路：先将数组排序(升序)，利用双指针，根据临时结果 和target的大小
来左右移动指针，当结果符合时，直接输出，
因为根据均值不等式，和相等时，差距越大的，乘积越小，2*4 < 3*3
所以，当从小往大，遍历时，找到时就可以输出了
'''
class Solution:
    def FindNumbersWithSum(self, array, target):
        size = len(array)
        if size < 1:return []
        left,right = 0,size-1
        temp = 0
        while left < right:
            temp = array[left] + array[right]
            if temp == target:
                return [array[left],array[right]]
            elif temp < target:
                left += 1
            else:
                right -=1
        return []

if __name__ == '__main__':
    so = Solution()
    nums= [1,2,3,4,5,6]
    target = 6
    res = so.FindNumbersWithSum(nums,target)
    print(res)
