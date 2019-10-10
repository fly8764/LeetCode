'''
方法一：位运算
0到n一共n+1个数字，取其中的n个数字，给定的索引0到n-1,
异或操作，每个数字和自身异或结果为0，零与其他值异或还等于其他值
所以，补充一个索引，使得索引从0到n完整，然后和数组中的值累积异或，
剩下的值就是缺失元素。
T(n) = n  O(n) = o(l)

方法二：
类似于上面的位运算，不过使用的数值求和 做差，
思路源自于 等差数列求和，正常的和为0-n，实际数组缺失一个元素，
两者逐项做差 并求和即可。主要防止 整型溢出。
T(n) = n  O(n) = o(l)

方法三：
哈希表 T(n) = n  O(n) = o(n)

方法四：
排序 T(n) = nlogn  O(n) = o(l)
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        res = 0
        #先和新加的索引异或一下
        res ^= size
        #在逐项的异或
        for i in range(size):
            res ^= i ^ nums[i]
        return res

    def missingNumber1(self, nums):
        size = len(nums)
        res = 0
        #先新加的索引 累加，新索引的填充值为0
        res += size
        for i in range(size):
            res += i- nums[i]
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.missingNumber([3,0,1]))
    print(so.missingNumber([9,6,4,2,3,5,7,0,1]))

