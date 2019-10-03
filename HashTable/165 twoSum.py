class Solution:
    def twoSum(self, nums, target):
        size = len(nums)
        if size < 2:return
        left,right = 0,size-1
        while left < right:
            temp = nums[left] + nums[right]
            if temp == target:
                return [left+1,right+1]
            elif temp < target:
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            else:
                right -= 1
                while right > left and nums[right]==nums[right+1]:
                    right -= 1
        return


if __name__ == '__main__':
    so = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(so.twoSum(nums,target))