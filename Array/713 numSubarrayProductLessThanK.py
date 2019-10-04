class Solution1:
#双指针，链表中 会有较多的指针
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

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        size = len(nums)
        res = []
        cur = []
        temp = 1
        for i in range(size):
            if temp *nums[i] < k:
                temp *= nums[i]
                cur.append(nums[i])
            else:
                sub = []
                for item in cur:
                    sub.append(item)
                    res.append(sub)
                if nums[i] < k:
                    cur = [nums[i]]
                    temp = nums[i]
                else:
                    temp = 1
                    cur = []
        return res




if __name__ == '__main__':
    so = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    res = so.numSubarrayProductLessThanK(nums,k)
    print(res)

