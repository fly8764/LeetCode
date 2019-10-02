class Solution:
    def searchInsert(self,nums,target):
        size = len(nums)
        if size < 1:return 0
        #为了保证目标值在 左右边界内
        left,right = 0,size
        while left < right:
            mid = (left+right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    # def searchInsert(self, nums, target):
    #     size = len(nums)
    #     if not size: return
    #     left, right = 0, size -1
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if nums[mid] == target:return mid
    #
    #         if nums[mid] < target:
    #             left = mid +1
    #         else:
    #             right = mid
    #     # if nums[left] == target:
    #     #     return left
    #
    #     if nums[left] > target:
    #         return left
    #     else:
    #         return left+1

if __name__ == '__main__':
    so = Solution()
    nums = [1,3,5,6] #[1]
    target = 5 #5,2,7,0
    # res1 = so.searchInsert(nums,1)
    # print(res1)
    res1 = so.searchInsert(nums,5)
    res2 = so.searchInsert(nums,2)
    res3 = so.searchInsert(nums,7)
    res4 = so.searchInsert(nums,0)
    print(res1,res2,res3,res4)