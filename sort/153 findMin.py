'''
思路：二分法
通过左边界 或 右边界 来找到 有序区间；
如果有序区间在 右边，则 最小值在左边 包括右边界 nums[left:mid]
如果有序区间在左边 nums[mid] > nums[right]，则最小值在右边，nums[mid:]
最终，二分到最后只有一个值，就是最小值。
'''
class Solution1:
    def findMin(self, nums):
        size = len(nums)
        if size < 1:return None
        left,right = 0,size-1

        while left < right:
            mid = (left + right)>>1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

'''
2020/12/2 23:19
二分法
题目给的数组是有序的，找到某个值，可以考虑使用二分法。
'''
class Solution:
    def findMin(self, nums):
        n = len(nums)
        left,right = 0,n-1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]



if __name__ =='__main__':
    so = Solution()
    print(so.findMin([3,4,5,1,2]))
    print(so.findMin([4,5,6,7,0,1,2]))
    print(so.findMin([1]))


