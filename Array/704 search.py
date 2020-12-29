class Solution1:
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


'''
2020/12/2 22:33
死循环主要是考虑到mid的取值方式、left的赋值方式以及while的循环条件，
left,right = 0,len(nums)-1
while left < right:
    mid = (left +right) >> 1 # 向下取整，
    if nums[mid] < target:
        left = mid  # 此时容易死循环
        
当left+right为奇数，left = right-1，左右非常接近时，如（5,6）
经过 mid = (left +right) >> 1，其实mid = left，
则如果用left = mid来更新left，则会进入死循环。

最后while循环结束出来时，要保证nums[left] == target。
因为有时left == right 使得循环结束，此时无法计算mid，不会return mid。
第二次做该题时，就犯了这个错误。
'''
class Solution:
    def search(self, nums, target):
        n = len(nums)
        if n < 1 or nums[0] > target or nums[-1] < target:
            return -1

        left,right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            return left
        else:
            return -1


if __name__ == '__main__':
    so = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    res = so.search(nums,target)
    print(res)
