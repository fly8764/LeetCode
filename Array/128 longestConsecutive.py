'''
方法一：先排序，然后按照逻辑关系，来计算以当前位置i为结尾的连续序列的长度，
然后再和最大长度比较，
时间复杂度：排序 o(nlogn),循环 o(n) T(n)= o(nlogn)

方法二：
使用一个集合，把数组去重，
每次大循环，找到一个新的起点num，如何判断新的起点，集合中没有 num-1，
然后每次从起点出发，每次递增1，new ，判断集合中是否存在new，存在就累计加1，
最后再和最大值比较，
从而实现题目要求的 o(n)时间复杂度
'''
class Solution:
    def longestConsecutive1(self, nums):
        size = len(nums)
        if size < 2:return size
        nums.sort()
        # print(nums)
        dp = [1]*size
        for i in range(1,size):
            if nums[i] == nums[i-1]:
                dp[i] = dp[i-1]
                continue
            elif nums[i] == 1+ nums[i-1]:
                dp[i] = dp[i-1] + 1
            # for j in range(i):
            #     if nums[i] == 1 + nums[j]:
            #         dp[i] = max(dp[i],dp[j] + 1)

        # print(dp)
        return max(dp)

    def longestConsecutive(self, nums):
        nums = set(nums)
        res = 0
        for num in nums:
            if not (num-1) in nums:
                curNum = num
                curCnt = 1
                while (curNum + 1) in nums:
                    curNum += 1
                    curCnt += 1
                res = max(res,curCnt)
        return res


if __name__ == '__main__':
    so = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(so.longestConsecutive(nums))
    nums = [0,1,1,2]
    print(so.longestConsecutive(nums))