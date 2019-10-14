'''
贪心算法
分两种情况，从左到右，升序和降序
两次遍历，升序：先从左到右，如果右边的值大于当前的值，则右边的孩子要比当前孩子多一个糖果
这种情况在遍历 1 2 3 3 2 1时，出错，因为这里只考虑右边比当前大的情况，
如果当前值比右边的值大呢？当前值减一，不行，当前值加1，多了；
所以还有从右往左再遍历一次
降序：从右往左：如果当前值比左边的小，则左边的值比当前值大一
都是处理“下一位”，不处理当前
'''
class Solution:
    def candy(self, ratings):
        size = len(ratings)
        candy = [1]*size
        candy[0] = 1
        for i in range(size-1):
            if ratings[i] < ratings[i+1]:
                candy[i+1] = candy[i] + 1

        for i in range(size-1,0,-1):
            if ratings[i-1] > ratings[i] and candy[i-1] <= candy[i]:
                candy[i-1] = candy[i] + 1
        return sum(candy)

class Solution1:
    def candy(self, nums):
        size = len(nums)
        if size < 1:
            return 0
        dp = [1]*size
        for i in range(size-1):
            if nums[i+1] > nums[i]:
                #这里直接加一，明显不对，反例，1，2，3，4，单单的加一肯定不对
                #应该在低级别的基础上加1
                # dp[i+1] += 1
                dp[i+1] = dp[i] + 1
        for j in range(size-1,0,-1):
            if nums[j-1] > nums[j] and dp[j-1] <= dp[j]:
                # dp[j-1] += 1
                dp[j-1] = dp[j] + 1
        return sum(dp)





if __name__ == '__main__':
    so = Solution1()
    print(so.candy([1,0,2]))
