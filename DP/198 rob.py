class Solution1:
    #这种动态规划，取最优有些特殊
    # dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])
    # 取当前的nums[i]，肯定比不取要多；
    # 然后就是 比较前面第二位，第三位的最大值，
    #最终的最大值，要考虑最后一个取或不取，max(dp[-1],dp[-2]),
    def rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0

        if size <3:
            return max(nums)

        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2]+nums[0]

        for i in range(3,size):
                dp[i] = max(dp[i-2],dp[i-3])+nums[i]

        return max(dp[-1],dp[-2])

class Solution:
    def rob(self, nums):
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


if __name__ == '__main__':
        so = Solution()
        res = so.rob([2,7,9,3,1])
        print(res)

        res = so.rob([2,1,1,2])
        print(res)


