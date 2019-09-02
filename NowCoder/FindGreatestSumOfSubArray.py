# -*- coding:utf-8 -*-
#19:39--19:50 11mins
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:return
        size = len(array)
        dp = [array[0]]*size
        res = array[0]
        for i in range(1,size):
            dp[i] = max(dp[i-1],0) + array[i]
            res = max(res,dp[i])

        return res


if __name__ == '__main__':
    so = Solution()
    nums = [6,-3,-2,7,-15,1,2,2]
    res = so.FindGreatestSumOfSubArray(nums)
    print(res)
