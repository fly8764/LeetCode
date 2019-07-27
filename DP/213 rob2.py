class Solution:
    #掐头去尾
    #为了不受尾的影响，直接把尾 截掉，此时不用尾，头可用，可不用
    #对等，为了不受头影响，直接把头去掉，此时不用考虑头，尾可用可不用，
    #一共三种结果，取最大值，
    #为了防止受影响，直接把头或者尾去掉一个
    def rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0

        if size < 4:
            return max(nums)

        return max(self._rob(nums[0:-1]),self._rob(nums[1:]))

    def _rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0

        if size < 3:
            return max(nums)

        dp = [0] * size
        dp[0] = nums[0]
        # dp[1]不是直接等于nums[1],而是max(nums[0],nums[1])
        dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    res = so.rob([1,2,1,1])
    print(res)

    res = so.rob([1,1,1,2])
    print(res)

    res = so.rob([2,1,1,2])
    print(res)

