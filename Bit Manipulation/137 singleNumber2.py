class Solution(object):
    # 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。
    # 找出那个只出现了一次的元素。
    def singleNumber(self, nums):
        #使用哈希表，字典，其pop(key) 使用的是关键字 popitem() 返回的是键值对
        # 这种哈希表更加节省时间和空间
        """
        :type nums: List[int]
        :rtype: int
        """
        res = dict()
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res.pop(num)
        return res.popitem()[0]

