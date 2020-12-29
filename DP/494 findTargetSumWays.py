class Solution1:
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

'''
题解链接
https://leetcode-cn.com/problems/target-sum/solution/huan-yi-xia-jiao-du-ke-yi-zhuan-huan-wei-dian-xing/
转化成求解01背包问题，即new_nums中的物品，组合成target重量的组合数。
'''
class Solution:
    def findTargetSumWays(self, nums, S):
        sum_value = sum(nums)
        if sum_value < S or (sum_value + S) & 1:
            return 0

        n_zero = 0
        new_nums = []
        for num in nums:
            if num == 0:
                n_zero += 1
            else:
                new_nums.append(num)

        # target = (S + sum_value)>>1
        target = (S + sum_value)//2
        '''
        这里的dp状态数组没有使用01背包中的初始化，把第一件物品的情况写进去，原因如下所示。
        所以一上来状态dp是个辅助数组，代表不使用商品时，组合成各个重量的组合数，因此dp[0]=1。
        '''

        dp = [0]*(target+1)
        dp[0] = 1
        # 这种写法当遇到[1000] -1000时会出问题
        # dp[new_nums[0]] = 1
        # for i in range(1,len(new_nums)):
        #     for j in range(target,new_nums[i]-1,-1):
        #         dp[j] += dp[j-new_nums[i]]

        for num in new_nums:
            for j in range(target,num-1,-1):
                dp[j] += dp[j-num]

        return dp[-1]*(1<<n_zero)





if __name__ =='__main__':
    so = Solution()
    # res = so.findTargetSumWays([1, 1, 1, 1, 1],3)
    res = so.findTargetSumWays([1000],-1000)
    print(res)

