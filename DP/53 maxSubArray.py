class Solution():
    def __init__(self):
        pass

    def maxSubArray(self,nums):
        length = len(nums)
        if length== 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0:length//2])
            max_right = self.maxSubArray(nums[length//2:])

        temp_l = 0
        max_tmp_l = nums[length//2-1]
        for i in range(length//2-1,-1,-1):
            temp_l += nums[i]
            max_tmp_l = max(max_tmp_l,temp_l)

        tmp_r = 0
        max_tmp_r = nums[length//2]
        for j in range(length//2,length):
            tmp_r += nums[j]
            max_tmp_r = max(max_tmp_r,tmp_r)

        tmp = max_tmp_l+ max_tmp_r

        return max(max_left,max_right,tmp)



    def maxSubArray1(self, nums):
        pass
        temp = nums[0]
        max_ = temp

        for i in range(1, len(nums)):
            if temp > 0:
                temp += nums[i]

            else:
                temp = nums[i]
            max_ = max(temp, max_)

        return max_

if __name__ == '__main__':
    so = Solution()
    res = so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)