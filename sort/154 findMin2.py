'''
思路和上一题 153 及 81类似
方法一：整体 往数组中间移动，当右移 左移 遇到相同的值时，继续移动，即可。

方法二：根据mid 和 右边界 的大小来判断，
特殊情况，nums[mid] == nums[right]时，right -= 1，来 逐渐缩小 右边界，不会遗漏最小值
(不用考虑 左边重复值的情况，因为 比较都在和右边界)
'''
class Solution:
    def findMin(self, nums):
        size = len(nums)
        if size < 1:return None
        left,right = 0,size -1

        while left < right:
            mid = (left + right)>>1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]

    # def findMin(self, nums):
    #     size = len(nums)
    #     if size < 1:return None
    #
    #     left,right = 0,size -1
    #     while left+1 < right and nums[left] == nums[left+1]:
    #         left += 1
    #     while right -1 > left and nums[right] == nums[right-1]:
    #         right -= 1
    #
    #     while left < right:
    #         mid = (left + right) >> 1
    #         if nums[mid] > nums[right]:
    #             left = mid + 1
    #             while nums[left] == nums[left-1] and left < right:
    #                 left += 1
    #         else:
    #             right = mid
    #             while right -1 > left and nums[right] == nums[right-1]:
    #                 right -= 1
    #     return nums[left]


if __name__ == '__main__':
    so = Solution()
    print(so.findMin([1,3,5]))
    print(so.findMin([2,2,2,0,1]))


