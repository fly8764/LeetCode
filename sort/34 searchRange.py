class Solution:
    def searchRange(self, nums, target):
        size = len(nums)
        if size < 1:return [-1,-1]
        left,right = 0,size-1
        while left < right:
            mid = (left+right)>>1
            if nums[mid] <target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            idx = left
            right = left + 1
            while right < size and nums[right] == target:
                right += 1
            return [left,right-1]
        else:
            return [-1,-1]


if __name__ == '__main__':
    so = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    res = so.searchRange(nums,target)
    print(res)

    nums = [5,7,7,8,8,10]
    target = 6
    res = so.searchRange(nums,target)
    print(res)

