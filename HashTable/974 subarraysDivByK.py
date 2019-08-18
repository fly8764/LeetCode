class Solution:
    #这题 k >2，所以不用考虑k=0 的情况
    def subarraysDivByK(self, nums, k):
        # 从左往右累计求和时，每次保存当前位置累计和的取余结果
        size = len(nums)
        if not size: # k= 0 不能直接排除
            return 0

        map = {}
        map[0] = 1 #初始化 对应于一上来就满足要求的情况,1代表这个 子串本身
        zero = {}
        zero[0] = 1
        summ = 0
        cnt = 0
        for i in range(size):
            summ += nums[i]
            if k:
                summ %= k
                if summ in map:
                    cnt += map.get(summ)
                map[summ] = 1 + map.get(summ,0)
            else:
                if summ in  zero:
                    cnt += zero[summ]
                zero[summ] = 1+ zero.get(summ,0)
        return cnt






    # def subarraysDivByK(self, nums, k):
    #     #暴力法，超时
    #     size = len(nums)
    #     if not size or not k:
    #         return 0
    #     dp = [0]*(size+1)
    #     cnt = 0
    #     for i in range(1,size+1):
    #         dp[i] = dp[i-1]+ nums[i-1]
    #
    #     for l in range(size):
    #         for r in range(l+1,size+1):
    #             sub = dp[r]- dp[l]
    #             if sub % k == 0:
    #                 cnt += 1
    #     return cnt


if __name__ == '__main__':
    so = Solution()
    nums = [4,5,0,-2,-3,1]
    k = 5
    res = so.subarraysDivByK(nums,k)
    print(res)


