class Solution1:
#双指针
    def numSubarrayProductLessThanK(self, nums, k):
        size = len(nums)
        if k <= 1: #由于数组中都是整数，所以不会有值小于1
            return 0
        prod = 1
        cnt = left = 0
        for right,value in enumerate(nums):
            prod *= value
            while prod >= k: #题目中要求 必须小于k，所以当等于k时，左指针也要右移
                prod /= nums[left]
                left += 1
            cnt += right - left + 1
        return cnt

'''
使用双指针，
当前累积小于k时，右指针right右移，同时乘以nums[right];
当前累积大于k时，左指针left右移，同时除以nums[left];
'''
class Solution:
    # def numSubarrayProductLessThanK(self, nums, k):
    #     #这种方法无法接触到最后一段符合要求的子序列，
    #     size = len(nums)
    #     res = []
    #     cur = []
    #     temp = 1
    #     for i in range(size):
    #         if temp < k:
    #             sub = []
    #             for item in cur:
    #                 sub.append(item)
    #                 res.append(sub)
    #         if temp *nums[i] < k:
    #             temp *= nums[i]
    #             cur.append(nums[i])
    #         else:
    #             if nums[i] < k:
    #                 cur = [nums[i]]
    #                 temp = nums[i]
    #             else:
    #                 temp = 1
    #                 cur = []
    #     return res

    def numSubarrayProductLessThanK(self, nums, k):
        size = len(nums)
        #下面是判断 目标值k是否满足条件，不是size大小，由于都是正整数，所以不会小于1
        if k <= 1:return 0
        cnt = 0
        cur = 1
        left = 0
        for right,value in enumerate(nums):
            cur *= value
            while cur >= k:
                cur /= nums[left]
                left += 1
            cnt += right - left + 1
        return cnt

if __name__ == '__main__':
    so = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    res = so.numSubarrayProductLessThanK(nums,k)
    print(res)

