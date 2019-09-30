# class Solution:
#     #贪心算法：一定长度的最长递增子序列 里 尾值最小的序列
#     #二分查找：寻找 左边第一个大于当前值的 位置
#     def lengthOfLIS(self, nums):
#         size = len(nums)
#         if size < 2: return size
#
#         tail = [nums[0]]
#         for i in range(1,size):
#             if nums[i] > tail[-1]:
#                 tail.append(nums[i])
#                 continue
#             left,right = 0,len(tail)-1
#             while left < right:
#                 # mid = left + (right - left)//2
#                 mid = (left + right)//2
#
#                 if tail[mid] < nums[i]:
#                     # 这里注意 mid + 1，而right直接等于mid，
#                     # 因为这里找的是 第一个大于nums[i]的值，而不是等于，所以要加1
#                     left = mid + 1
#                 else:
#                     right = mid
#             tail[left] = nums[i]
#
#         return len(tail)

#second
# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
class Solution:
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
                if nums[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            #最终一定会找到 第一个大于nums[i]的值的位置
            #更新后的tail并不是真正的LTS，但tail的长度代表此时的最大长度
            #更新后，只代表有可能使得后面的长度更长，（贪心算法）
            tail[left] = nums[i]
        return len(tail)

if __name__ == '__main__':
    so = Solution()
    s = [10,9,2,5,3,7,101,18]
    res = so.lengthOfLIS(s)
    print(res)


