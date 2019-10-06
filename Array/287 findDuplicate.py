class Solution(object):
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #字典 哈希表
        table = set()
        for num in nums:
            if num not in table:
                table.add(num)
            else:
                return num

    def findDuplicate2(self, nums):
        #排序，二分查找
        pass

    def findDuplicate(self, nums):
        #inplace 交换
        pass

