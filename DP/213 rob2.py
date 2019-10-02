class Solution:
    def rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0

        if size < 4:
            return max(nums)

        # if size == 3:
        #     return max(nums)

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        flag = [0] * size
        flag[0] = 1
        flag[1] = 0
        flag[2] = 1

        for i in range(3, size):
            if dp[i - 2] > dp[i - 3]:
                dp[i] = dp[i - 2] + nums[i]
                flag[i] = flag[i - 2]
            else:
                dp[i] = dp[i - 3] + nums[i]
                flag[i] = flag[i - 3]

        if dp[-1] > dp[-2] and flag[-1] != 0:
            return dp[-1]
        else:
            return dp[-2]

class Solution1:
    def find(self, nums):
        size = len(nums)
        #对于空列表要单独计算
        if size < 1:return 0
        if size < 3:return max(nums)
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,size):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]

    def rob(self,nums):
        if len(nums) < 1:
            return 0
        # 要考虑只有一个数子的情况,没法 掐头去尾
        if len(nums) < 2:
            return nums[0]

        res1 = self.find(nums[1:])
        res2 = self.find(nums[:-1])
        return max(res1,res2)