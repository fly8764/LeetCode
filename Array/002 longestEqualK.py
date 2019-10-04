class Solution:
    def longestEqualK(self,nums,k):
        size = len(nums)
        dic = {}
        #至关重要的一步，位置-1的累加和为0
        #因为位置都是从下标0开始的，所以当summ == k时，长度为i+1，而不是i
        #如果下标从1开始，则dic[0] = 0，总之，dic[0]要提前设定好
        dic[0] = -1
        summ = 0
        maxx = 0
        for i in range(size):
            summ += nums[i]
            if summ-k in dic:
                # 长度不是i - j + 1，因为j不在子序列内
                # maxx = max(maxx,i-dic[summ-k]+1)
                maxx = max(maxx,i-dic[summ-k])
            #注意这里的条件不是简单的是上面if的反面，不是一个逻辑
            if summ not in dic:
                dic[summ] = i #这里只需要保存一次即可，刚上来最左边的位置下标
        return maxx


if __name__ == '__main__':
    so = Solution()
    nums= [7,3,2,1,1,7,-6,-1,7]
    k = 7
    print(so.longestEqualK(nums,k))