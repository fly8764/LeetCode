class Solution:
    def maxSubArray(self, nums):
        temp = nums[0]
        max_ = temp

        for i in range(1, len(nums)):
            if temp > 0:
                temp += nums[i]
            else:
                temp = nums[i]
            max_ = max(temp, max_)
        return max_

    def maxSubArray1(self, nums):
    # T(n) = n   O(n) = o(l)
        temp = nums[0]
        maxx = temp
        for i in range(1,len(nums)):
            if temp > 0:
                temp += nums[i]
            else:
                temp = nums[i]
            maxx = max(maxx,temp)
        return maxx

    def find(self,nums):
        size = len(nums)
        res = 0
        dp = [0]*size
        dp[0] = nums[0]
        summ = nums[0]
        for i in range(1,size):
            if summ > 0:
                summ += nums[i]
            else:
                summ = nums[i]
            res = max(res,summ)
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.find([-2,1,-3,4,-4,2,1,-5,4]))