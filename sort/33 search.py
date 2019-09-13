'''
思路：
根据mid和左边界或有边界比较，来找到有序区间和无序区间；
然后在有序区间 判读target是否在 能够肯定的有序区间，
若不在，则 从两边往中间缩小区间；

'''
class Solution:
    def search(self, nums, target):
        size = len(nums)
        if size < 1:return -1
        left,right = 0,size-1
        while left < right:
            mid = (left+right)>>1
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                #右区间有序
                if nums[mid] < target <= nums[right]:
                    # 判断是否在 可以肯定的区间内
                    left = mid + 1
                else:
                    right = mid -1
            else:
                #左区间有序
                if nums[left] <= target < nums[mid]:
                    #判断是否在 可以肯定的区间内
                    right = mid -1
                else:
                    left = mid + 1

        if nums[left] == target:
            return left
        else:
            return -1

    # def search(self, nums, target):
    # 错误解法
    #     size = len(nums)
    #     if size < 1:return -1
    #     left, right = 0,size-1
    #     while left < right:
    #         mid = (left + right)>> 1
    #         if nums[mid] == target:
    #             return mid
    #         if nums[mid] > target:
    #             if nums[0] > target:
    #                 left = mid #不加 1
    #             else:
    #                 right = mid
    #         else:
    #             left = mid + 1
    #     if nums[left] == target:
    #         return left
    #     return -1


if __name__ == '__main__':
    so = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    res = so.search(nums,target)
    print(res)
    print(so.search(nums = [4,5,6,7,0,1,2], target = 3))

