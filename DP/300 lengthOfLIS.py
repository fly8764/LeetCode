class Solution:
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


if __name__ == '__main__':
    so = Solution()
    s = [10,9,2,5,3,7,101,18]
    res = so.lengthOfLIS(s)
    print(res)


