'''
思路和上一题 153 及 81类似
方法一：整体 往数组中间移动，当右移 左移 遇到相同的值时，继续移动，即可。

方法二：根据mid 和 右边界 的大小来判断，
特殊情况，nums[mid] == nums[right]时，right -= 1，来 逐渐缩小 右边界，不会遗漏最小值
(不用考虑 左边重复值的情况，因为 比较都在和右边界)
'''
class Solution1:
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

    def findMin1(self, nums):
        size = len(nums)
        if size < 1:return None

        left,right = 0,size -1
        while left+1 < right and nums[left] == nums[left+1]:
            left += 1
        while right -1 > left and nums[right] == nums[right-1]:
            right -= 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
            else:
                right = mid
                while right -1 > left and nums[right] == nums[right-1]:
                    right -= 1
        return nums[left]

'''
2020/12/2 23:53
这题增加了重复值的情况，对于重复值不在旋转点的情况，影响不大，考察点在旋转点在重复值中，如[3,3,1,3]
一般可以在移动前后比较，决定是否再重新移动一位，这中直接的方法可以通过。

方法一 和153题和81题类似
把左右两边往中间移动，移动后发现和移动前的值相等，继续往中间移动。

方法二 只对右指针的重复值进行再移动
由于mid受左右指针的影响，只要改变一个，mid就会改变，然后左右指针也会改变。
所以对于 mid == right 的情况，可以把right再往中间移动，来观察结果。

第二次做该题时，没有想到方法二。
'''
class Solution:
    def findMin(self, nums):
        n = len(nums)
        left,right = 0,n-1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]



if __name__ == '__main__':
    so = Solution()
    print(so.findMin([1,3,5]))
    print(so.findMin([2,2,2,0,1]))


