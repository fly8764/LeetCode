'''
右边界不断右移，计算以右边界i为结尾的子序列的累计和summ，
当summ>=k时，不断缩小左边界；同时，和最终结果比较，并更新
'''
class Solution:
    def shortestSubarray(self, nums, k):
        size = len(nums)
        minn = float('inf')
        summ,left = 0,0
        #summ：以right为右边界的子序列的累计和，左边界在不断地变化，并且不是每次来个新的right，left都重新置0
        for right in range(size):
            #特殊情况，单个元素即满足要求
            if nums[right] >= k:
                return 1
            summ += nums[right]
            #如果当前的累计和小于等于0，则此时的子序列对增大累计和没有帮助，所以清空
            #left = right + 1
            if summ < 1:
                summ = 0
                left = right + 1
                continue
            #特殊情况，当遇到一个nums[i]远小于0，或其周围都是负数，则其对结果也没有帮助,
            #但summ依然大于等于k，此时，把左边界往右移，减小summ，
            #将这种负数往前累加，同时把沿途的值置为0
            #这样能够极大加快左边界left的往右移动的速度，从而表面上看是o(n^2)，实际上要小于这种复杂度
            #这一点在下面的操作中尤为明显
            #这里也不担心j < 0 呢？
            j = right -1
            while nums[j+1] < 0:
                nums[j] += nums[j+1]
                nums[j+1] = 0
                j -= 1
            if summ >= k:
                while summ - nums[left] >= k or nums[left] <=0:
                    #这里的nums[left]主要为上面的更新考虑的，不太能理解
                    summ -= nums[left]
                    left += 1
                minn = min(minn,right -left+1)
        if minn == float('inf'):
            return -1
        else:
            return minn

    # def shortestSubarray(self, nums, k):
    #     #不大于k的子序列中的最长子序列 方法 简单改动后，不行
    #     size = len(nums)
    #     summ = [0]*size
    #     emap = [0]*size
    #     summ[-1] = nums[-1]
    #     emap[-1] = size-1
    #     for i in range(size-2,-1,-1):
    #         if summ[i+1] >=0:
    #             summ[i] = nums[i]
    #             emap[i] = i
    #         else:
    #             summ[i] += summ[i+1] + nums[i]
    #             emap[i] = emap[i+1]
    #     start = 0 #右边界
    #     s = 0
    #     minn = float('inf')
    #     for i in range(size-1):
    #         while start < size and s+summ[start] <= k:
    #             s += summ[start]
    #             start = emap[start]+1 #从右边界的下一个位置再次计算，累加
    #         #下一轮从i+1开始
    #         # 累计求和大于k,从i+1继续开始，累计和s-=nums[i]（分情况讨论）
    #         # 如果start == i，即上来summ[i]就大于k，则不进行操作，
    #         # 因为，s没有进行累加s += summ[start]
    #         if start > i:
    #             s -= nums[i]
    #         # if s >=k:
    #         #     minn = min(minn, start - i)
    #         minn = min(minn,start-i)
    #         # minn = max(minn,start-i)
    #         start = max(start,i+1)
    #     if minn == float('inf'):
    #         return -1
    #     else:
    #         return minn

if __name__ == '__main__':
    so = Solution()
    nums = []
    k = 0
    print(so.shortestSubarray(nums = [1], k=1))
    print(so.shortestSubarray(nums = [1,2], k = 4))
    print(so.shortestSubarray(nums = [2,-1,2], k = 3))

