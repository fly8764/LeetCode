class Solution1:
    #贪心算法：一定长度的最长递增子序列 里 尾值最小的序列
    #二分查找：寻找 左边第一个大于当前值的 位置
    def lengthOfLIS(self, nums):
        size = len(nums)
        if size < 2: return size

        tail = [nums[0]]
        for i in range(1,size):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            left,right = 0,len(tail)-1
            while left < right:
                # mid = left + (right - left)//2
                mid = (left + right)//2

                if tail[mid] < nums[i]:
                    # 这里注意 mid + 1，而right直接等于mid，
                    # 因为这里找的是 第一个大于nums[i]的值，而不是等于，所以要加1
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]

        return len(tail)

#second
# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
class Solution2:
    def lengthOfLIS(self,nums):
        size = len(s)
        if size < 2:return size

        tail = [nums[0]]
        for i in range(1,size):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            left,right = 0,len(tail)-1
            #比较好用的二分查找法
            while left < right:
                mid = (left + right)>>1
                #mid = (left + right)>>1 奇数时，mid偏左边，对应的left = mid + 1，否则 死循环
                #区别于 mid =(left+right+1)>>1 奇数时，mid偏右边 right = mid -1
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            #最终一定会找到 第一个大于nums[i]的值的位置
            #更新后的tail并不是真正的LTS，但tail的长度代表此时的最大长度
            #更新后，只代表有可能使得后面的长度更长，（贪心算法）
            tail[left] = nums[i]
        return len(tail)


'''
2020/12/2 0:23
方法一 动态规划
定义状态dp[i],以nums[i]为结尾的上升子序列的长度，对于每个dp[i],要把前面的dp遍历一遍，
找到其中满足 nums[j] < nums[i]的子序列，在其基础上加1，再和当前的大小比较，选最大值。
时间复杂度：T(n) = o(n^2)

方法二 贪心 + 二分法 + 动态规划

长度一定的上升子序列，其末尾元素tail[-1]的值越小，这样后面才可能使子序列更长。
定义状态tail[i]，所有长度为i+1的上升子序列的结尾的最小值；过程中维护这个数组。
每来一个新的元素nums[i]，在有序数组tail中找到第一个大于nums[i]的元素，将其替换替换掉；
若没有，则把nums[i]放在tail后面，上升子序列的长度加一。
最终tail即为所求的最长公共子序列。
在有序数组中查找目标值的位置，可以使用二分查找。
时间复杂度：T(n) = o(nlogn) 主要在往回遍历时，这里使用的是有序数组，所有可以使用二分查找，
把时间复杂度降低到o(logn)
'''
class Solution:
    def lengthOfLIS1(self, nums):
        n = len(nums)
        if n < 1:
            return 0
        dp = [1]*n
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp)

    def lengthOfLIS(self, nums):
        n = len(nums)
        if n < 2:return n

        tail = [nums[0]]
        for i in range(1,n):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            left = 0
            right = len(tail) - 1
            # 找到第一个大于tail[-1]的位置left，把其替换掉，使得tail的尾部元素尽可能小。
            while left < right:
                # mid = left + (right - left) // 2
                mid = (left + right) >> 1
                # 这里的二分选择有讲究，需要研究一下
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]

        return len(tail)




if __name__ == '__main__':
    so = Solution()
    # s = [10,9,2,5,3,7,101,18]
    s = [4,10,4,3,8,9]
    res = so.lengthOfLIS(s)
    print(res)


