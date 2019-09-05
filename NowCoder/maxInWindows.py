# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self,num,k):
        size = len(num)
        if size < k or k < 1:
            return []
        res = []
        for i in range(size -k+1):
            res.append(max(num[i:i+k]))
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [2,3,4,2,6,2,5,1]
    k = 3
    res = so.maxInWindows(nums,0)
    print(res)