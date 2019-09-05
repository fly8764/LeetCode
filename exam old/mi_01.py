class Solution():
    #递归求解，容易超时，使用 动态规划，0-1背包问题 T(n) = n,
    #暴力递归 超时
    # def __init__(self):
    #     self.target = 0
    #     self.flag = 0

    # def dfs(self,nums,cur):
    #     if cur == self.target:
    #         self.flag = 1
    #         return
    #
    #     size = len(nums)
    #     if not size:
    #         return
    #
    #     for i in range(size):
    #         if self.flag :return
    #         self.dfs(nums[:i] + nums[i + 1:], cur)
    #
    #         if cur+nums[i] <= self.target:
    #             self.dfs(nums[:i] + nums[i + 1:], cur + nums[i])
    #             if self.flag: return
    #
    #         else:
    #             break

    # def dfs(self,start,cur):
    #     if cur == self.target:
    #         self.flag = 1
    #         return
    #     for i in range(start,self.n):
    #         if nums[i] + cur > self.target:
    #             break
    #
    #         if i > 0 and nums[i] > nums[i-1]:
    #             continue
    #
    #         if nums[i] + cur == self.target:
    #             self.flag = 1
    #             return
    #         else:
    #
    #             self.dfs(i+1,cur+nums[i])

    # def find(self,nums,target):
    #     self.target = target
    #     self.n = len(nums)
    #     self.dfs(0,0)
    #     return self.flag
    def solver(self,nums,target):
        size = len(nums)
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(size):
            for j in range(target,nums[i]-1,-1):
                dp[j] = dp[j] or dp[j-nums[i]]

        return dp[-1]


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    target = int(input())
    so = Solution()
    nums.sort()
    res = so.solver(nums,target)
    print(res)



