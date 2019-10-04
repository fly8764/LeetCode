class Solution:
    def longestLowK(self,nums,k):
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
            while s+summ[start] <= k and start < size:
                s += summ[start]
                start = emap[start]+1 #从右边界的下一个位置再次计算，累加
            #下一轮从i+1开始
            # 累计求和大于k,从i+1继续开始，累计和s-=nums[i]（分情况讨论）
            # 如果start == i，即上来summ[i]就大于k，则不进行操作，
            # 因为，s没有进行累加s += summ[start]
            if start > i:
                s -= nums[i]
            maxx = max(maxx,start-i)
            start = max(start,i+1)
        return maxx


if __name__ == '__main__':
    so = Solution()
    nums = [100,200,7,-6,-3,100] #res:[7,-6,-3] 3
    k = 7
    print(so.longestLowK(nums,k))


