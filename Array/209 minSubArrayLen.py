'''
类似于leetcode 862一样，862 数组中还有负数和零
不过这题数组中均为正数，前缀和为递增序列，可以使用双指针法，来找到满足要求的子数组
'''
class Solution:
    def minSubArrayLen1(self, s, nums):
        size = len(nums)
        if size < 1:
            return 0
        summ,left,right = 0,0,0
        minn = float('inf')
        for right in range(size):
            if nums[right] >= s:
                return 1
            summ += nums[right]
            if summ < 1:
                left = right + 1
                continue
            j = right -1
            while j>=0 and nums[j+1] < 0:
                nums[j] += nums[j+1]
                nums[j] = 0
                j -= 1
            if summ >= s:
                while summ - nums[left] >= s or nums[left] <= 0:
                    summ -= nums[left]
                    left += 1
                minn = min(minn,right - left +1)
        if minn == float('inf'):
            return 0
        else:
            # return nums[left:right+1]
            return minn

    def minSubArrayLen2(self, s, nums):
        #双指针法，right向右移动增加值，当和大于等于k时，
        #left左移，不停地减小值，来寻找最短子数组
        size = len(nums)
        if size < 1:return 0
        res = float('inf')
        left = 0
        summ = 0
        for right in range(size):
            summ += nums[right]
            while summ >= s:
                res = min(res,right - left +1)
                summ -= nums[left]
                left += 1
        if res == float('inf'):
            return 0
        else:
            return res

    def find(self,nums,end,x):
        left,right = 0,end
        while left < right:
            mid = (left + right + 1)>>1
            if nums[mid] > x:
                right = mid -1
            else:
                left = mid

        if nums[left] > x:
            return -1
        else:
            return left

    def minSubArrayLen(self, s, nums):
        #前缀和  二分查找
        #计算出前缀和后，在当前点i的前面找到 小于等于 summ[i]-s的下标j
        #若j存在，则 length = i-j，不是i-j+1，
        #注意的细节，前缀和不一定必须包含数组中的元素，还有空前缀和，
        #这为了表示前i个元素之和满足要求
        size = len(nums)
        summ = [0]*(size+1)
        res = float('inf')
        for i in range(1,size+1):
            summ[i] = summ[i-1] + nums[i-1]

        for i in range(1,size+1):
            temp = summ[i] - s
            #不用考虑temp是否大于零，因为在summ中找不到比负数还小的值，返回值为-1
            left = self.find(summ, i - 1, temp)
            if left >= 0:
                res = min(res, i - left)

        if res == float('inf'):
            return 0
        else:
            return res


if __name__ == '__main__':
    so = Solution()
    print(so.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))
    print(so.minSubArrayLen(s = 167, nums = [84,-37,32,40,95]))