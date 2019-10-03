class Solution:
    def findLengthOfLCIS(self, nums):
        #使用一个临时变量，更加节省空间和时间复杂度
        size = len(nums)
        if size < 2:return size
        # dp = [1]*size
        maxx = 1
        cnt = 1
        for i in range(1,size):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            maxx = max(maxx,cnt)
        return maxx


if __name__ == '__main__':
    so = Solution()
    nums = [1,3,5,4,7]
    print(so.findLengthOfLCIS(nums))
    nums = [2]*5
    print(so.findLengthOfLCIS(nums))