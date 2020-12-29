class Solution1(object):
    #本题 考察的是位运算，相同的数字 异或 为0，任何数字与零异或 都等于本身
    def singleNumber0(self, nums):
        # 除了某个元素只出现一次以外，其余每个元素均出现两次
        # 因此，使用异或，两次相同的结果为0， 任何数字与零异或 都等于本身
        res = 0
        for item in nums:
            res ^= item
        return res

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

        # for key,value in res.items():
        #     if value == 1:
        #         return key
        #     else:
        #         continue


'''
2020/12/13 15:00
这题主要考察位运算

方法一 位运算-异或
0与任何数异或都等于数本身，任何数与自身异或都为0，
因此可以让0与和数组依次异或，最后的结果就是那个出现一次的数。


方法二 哈希表
动态空间，中间最多n/2个元素空间

'''
class Solution:
    # 位运算 异或 ^
    def singleNumber1(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return  res

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




if __name__ == '__main__':
    so = Solution()
    res = so.singleNumber([2,2,3,2])
    print(res)
    res = so.singleNumber([4,1,2,1,2])
    print(res)

