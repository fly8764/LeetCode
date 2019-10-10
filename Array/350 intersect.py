'''
方法一：使用两个字典，T(n) = n, O(n) = o(n)
方法二：先排序，使用两个指针，比较两个值，小的值右移；相等则加入到res中
T(n) = nlogn 主要用在排序上, O(n) = o(n)
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        #方法二：先排序，使用两个指针，比较两个值，小的值右移；相等则加入到res中
        size1 = len(nums1)
        size2 = len(nums2)
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        res = []
        while p1 < size1 and p2 < size2:
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                #下面两个右移别忘了，否则，死循环
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res


    def intersect1(self, nums1, nums2):
        #方法一：使用两个字典，T(n) = n, O(n) = o(n)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = {}
        dic2 = {}
        res = []
        for num in nums1:
            dic1[num] = dic1.get(num,0) + 1
        for num in nums2:
            dic2[num] = dic2.get(num,0) + 1

        for key,value in dic1.items():
            if key in dic2:
                res.extend([key]*min(value,dic2.get(key)))
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
    print(so.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))