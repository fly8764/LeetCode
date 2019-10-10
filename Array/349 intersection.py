'''
哈希表 集合
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1)&set(nums2))
    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set()
        for num in nums2:
            if num in nums1 and num not in res:
                res.add(num)
        return list(res)


if __name__ == '__main__':
    so = Solution()
    print(so.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
    print(so.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

