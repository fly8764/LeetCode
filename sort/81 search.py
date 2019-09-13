'''
思路：
相比于原始 33题，判断旋转数组中是否有所需元素，这里的数组中有连续的重复元素，
所以要考虑重复元素，当往数组中间移动时，要判断一下，如果重复，则再次往中间移动
'''

class Solution:
    def find(self,nums,target):
        size = len(nums)
        left,right = 0,size -1
        #这里要注意起始时 两端的重复元素；
        #同时，要注意 while A and B:  条件判断的先后顺序，当A不成立时，就不会在判断B了，
        # 所以要把 left+ 1 是否越界这个判断条件 放在前面(A),然后再索引
        while left+1 < right and nums[left+1] == nums[left]:
            left += 1
        while right -1 > left and nums[right-1] == nums[right] :
            right -= 1

        while left < right:
            mid = (left + right)>>1
            if nums[mid] == target:return mid
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                else:
                    right = mid -1
                    while nums[right] == nums[right+1] and right > left:
                        right -= 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                    while nums[right] == nums[right+1] and right > left:
                        right -= 1
                else:
                    left = mid + 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        if nums[left] == target:
            return left
        else:
            return -1

    def search(self, nums, target):
        size = len(nums)
        if size < 1:
            return False

        res = self.find(nums,target)
        if res != -1:
            return True
        else:
            return False

if __name__ == '__main__':
    so = Solution()
    # print(so.search(nums = [2,5,6,0,0,1,2], target = 0))
    # print(so.search(nums = [2,5,6,0,0,1,2], target = 3))
    # print(so.search(nums = [3,1,1], target = 3))
    # print(so.search(nums = [1,1,3,1], target = 3))
    print(so.search(nums = [1], target = 0))

