class Solution:
    def findTargetSumWays(self, nums, S):
        #判断是否为奇数，或者负数
        sum_value = sum(nums)
        if (sum_value < S or (sum_value+S) &1):
            return  0

        #去零，计零
        new_nums = []
        n_zero = 0
        for num in nums:
            if num == 0:
                n_zero +=1
            else:
                new_nums.append(num)

        x = (sum_value + S)>>1
        size = len(new_nums)
        dp = [0 for _ in range(x + 1)]
        dp[0] = 1
        for i in range(size):
            for j in range(x,new_nums[i]-1,-1):

                dp[j] += dp[j-new_nums[i]]

        return dp[-1]*(1<<n_zero)





if __name__ =='__main__':
    so = Solution()
    res = so.findTargetSumWays([1, 1, 1, 1, 1],3)
    print(res)

