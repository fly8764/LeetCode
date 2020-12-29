'''
2020/12/3 0:23
方法一 排序 找中间索引
把两个数组组合在一起后排序，然后找到中间的索引。
T(n) = o((m+n)log(m+n))
方法二 双指针 归并排序
两个数组各一个指针，从左到右，不断移动指针，比较大小，放到新的数组中，然后找到中间索引。

方法三
题目要求尽可能达到 T(n) = o(log(m+n))

'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        nums = nums1+nums2
        nums.sort()
        if n & 1:
            return nums[n>>1]*1.0
        else:
            return (nums[n>>1] + nums[-1 + n >> 1])/2


if __name__ == '__main__':
    func = Solution()
    # nums1,nums2 = [1,3],[2]
    nums1,nums2= [1,2],[3,4]
    print(func.findMedianSortedArrays(nums1,nums2))
