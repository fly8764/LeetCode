class Solution:
    #用目标和的方法做，太耗时，2608ms
    def canPartition1(self, nums):
        pass

    def canPartition(self, nums):
        sum_value = sum(nums)
        if (sum_value&1):
            return  False
        new_nums = nums

        x = sum_value >> 1
        size = len(new_nums)
        dp = [0]*(x + 1)
        dp[0] = 1

        for i in range(size):
        # 用目标和的方法做，不加这个判断条件，太耗时，2608ms，加了，就不用把所有的情况遍历一遍
            if dp[-1] != 0:
                return True

            for j in range(x,new_nums[i]-1,-1):
                dp[j] += dp[j-new_nums[i]]

        return dp[-1] != 0


if __name__ == '__main__':
    so = Solution()
    res = so.canPartition([1, 5, 11, 5])
    print(res)

    res = so.canPartition([1, 2, 3, 5])
    print(res)

    res = so.canPartition([1, 2, 5])
    print(res)

