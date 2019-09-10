class Solution:
    def canIWin(self, maxInt: int, target: int):
        size = maxInt
        nums = [i for i in range(1,maxInt+1)]
        # if size % 2 == 0 or size == 1:
        #     return True

        dp = [0] * size
        for i in range(size - 1, -1, -1):
            dp[i] = nums[i]
            for j in range(i + 1, size):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
                if dp[j] >= target:
                    return True

        return False
        # return dp[-1] >= 0


if __name__ == '__main__':
    so = Solution()
    res = so.canIWin(10,11)
    print(res)