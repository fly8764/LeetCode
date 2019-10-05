class Solution:
    def longestNotOverK(self,nums,k):
        size = len(nums)
        summ = [0]*size
        emap = [0]*size
        summ[-1] = nums[-1]
        emap[-1] = size-1
        for i in range(size-2,-1,-1):
            if summ[i+1] >=0:
                summ[i] = nums[i]
                emap[i] = i
            else:
                summ[i] += summ[i+1] + nums[i]
                emap[i] = emap[i+1]
        start = 0 #右边界
        s = 0
        maxx = 0
        for i in range(size-1):
            #这里while循环的两个条件有先后顺序，把start< size放在前面，如果这个条件不满足，
            # 则后面第二个条件就不会判断，同时summ[start]也越界
            #这里的循环条件 s+summ[start] <= k 是为了尽可能多的拉长子序列的长度，
            #while出来时保证 s<= k，可以直接计算长度，并和最终结果比较判断
            while start < size and s+summ[start] <= k:
                s += summ[start]
                start = emap[start]+1 #从右边界的下一个位置再次计算，累加
            #下一轮从i+1开始
            # 累计求和大于k,从i+1继续开始，累计和s-=nums[i]（分情况讨论）
            # 如果start == i，即上来summ[i]就大于k，则不进行操作，
            # 因为，s没有进行累加s += summ[start]
            if start > i:
                s -= nums[i]
            #这里不用担心 s> k and start >= size 的情况出现，
            #因为判断条件 会预先判读是否后大于k，大于k就不进行累加了
            #所以while循环出来时，s<= k,同时start是此次满足条件的右边界的下一位，
            #所以，长度 为start-i，而不是start-i+1
            maxx = max(maxx,start-i)
            start = max(start,i+1)
        return maxx


if __name__ == '__main__':
    so = Solution()
    nums = [100,200,7,-6,-3,100] #res:[7,-6,-3] 3
    k = 7
    print(so.longestNotOverK(nums,k))
    print(so.longestNotOverK(nums = [2,-1,2], k = 3))


