class Solution:
    #双指针的前提：有序数组，所以要先 排序，注意排除相同值的情况，左移或者右移后，
    #如果和上次的相同，则再移动一次
    def threeSum(self, nums):
        size = len(nums)
        if size <3:return []
        nums.sort()
        res = []
        for k in range(size-2):
            if nums[k] > 0:break
            if nums[k] == nums[k-1] and k >0:continue #这个细节非常重要
            i,j  = k+1,size-1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s == 0:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:j -= 1
                elif s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:i += 1
                else:#注意这个else 和前面的elif 对齐，说明是一个级别的
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:j -= 1

        return res


if __name__ == '__main__':
    so = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = so.threeSum(nums)
    print(res)