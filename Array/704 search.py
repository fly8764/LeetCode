class Solution:
    def search(self, nums, target):
        size = len(nums)
        left, right = 0, size -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:return mid
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1

        # if nums[left] > target:
        #     return left
        # else:
        #     return left+1



if __name__ == '__main__':
    so = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    res = so.search(nums,target)
    print(res)
