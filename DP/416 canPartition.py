'''
题目转化成01背包问题，拆分成两个子集，两个子集的和相等；
target = sum(nums) >> 1
即看能否找到一种组合，其和为target，这里只要找到即可，不需要像常规的动态规划，
找到所有的可能，所以每次循环都先看一下dp[target]是否符合要求，从而避免遍历所有的情况。
'''
class Solution1:
    #用目标和的方法做，太耗时，2608ms
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

# 2020/11/30 19:57
# 这一题题目有点不严谨，说了每个数组不能超过100，但是如果添加了这个限制条件就不能通过。
class Solution:
    def canPartition(self, nums):
        n = len(nums)
        # 如果和为奇数，则不存在可能
        if sum(nums) & 1:
            return False
        target = sum(nums) >> 1
        dp = [0] * (target+1)
        # dp[0] = 1别忘了
        dp[0] = 1
        # 这个dp[nums[0]] = 1 最好不要用，因为有时候target < nums[0]
        # dp[nums[0]] = 1
        for i in range(n):
            # 不同于目标和，找到所有的可能；这里只要能够找到满足条件的即可；
            # if dp[-1] > 0 and dp[-1] <= 100:
            if dp[-1] != 0:
                return True
            for j in range(target,nums[i]-1,-1):
                dp[j] += dp[j-nums[i]]

        return dp[-1] != 0

        # if dp[-1] > 0 and dp[-1] <= 100:
        #     return True
        # else:
        #     return False


if __name__ == '__main__':
    so = Solution1()
    res = so.canPartition([1, 5, 11, 5])
    print(res)

    res = so.canPartition([1, 2, 3, 5])
    print(res)

    res = so.canPartition([1, 2, 5])
    print(res)

