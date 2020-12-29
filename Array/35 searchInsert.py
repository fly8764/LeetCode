class Solution1:
    def searchInsert2(self,nums,target):
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

    def searchInsert(self, nums, target):
        size = len(nums)
        if not size: return
        left, right = 0, size -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:return mid

            if nums[mid] < target:
                left = mid +1
            else:
                right = mid
        # if nums[left] == target:
        #     return left

        if nums[left] > target:
            return left
        else:
            return left+1


'''
2020/12/2 0:28

'''
class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        if n < 1:return 0
        # 特判
        if nums[-1] < target:return n

        left,right = 0,n-1
        # 这里while循环找到的left，是第一个大于等于target的位置
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        # 最后返回结果时，别忘了有时没有相等的值的情况，需要放在left后面，即left+1
        if nums[left] > target:
            return left
        else:
            return left + 1


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