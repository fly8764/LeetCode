class Solution:
    # f(4) = (f(3) ) + (f(2) ) + (f(1) )
    # 以num为一个元素时，求 以i- num为和的情况有多少种
    # dp[i] =dp[i] + dp[i-num]
    def combinationSum4(self, nums, target):
        if len(nums) <1 or target<1:
            return 0

        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]

        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    res = so.combinationSum4([1, 2, 3],4)
    print(res)