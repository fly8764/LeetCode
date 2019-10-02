'''
哈希表（取模）
使用字典，从左往右求和，但是字典的键不保存实际和，而是mod k对应的值为当前的下标i；
往右求和的过程中，当在此遇到与之前相同余数的值(下标j)时，说明
nums[i + 1:j + 1]之间的数组串的实际和sum_是k的整数倍k×n(n > 0);
所以，当j - i > 1时，即可返回True。
因为，这里要求的是整除，所以只关心余数即可，取模(余)满足结合律。

这题主要使用的是数学方法，取余，而不是动态规划，动规咋做呢？
'''
class Solution1:
    def checkSubarraySum(self, nums, k):
        size = len(nums)
        if size < 2:
            return False
        temp = 0
        lookup = {}
        lookup[0] = -1 #这一初始化很重要，防止一上来第一个值就被k整除的特例
        for i in range(size):
            temp += nums[i]
            if  k:
                temp %= k
            #这个用法很好
            pre = lookup.get(temp,None)
            if pre != None:
                if i - pre > 1:
                    return True
            else:
                lookup[temp] = i
        return False

    # def checkSubarraySum(self, nums, k):
    #     #外层 起始点，内层终点，不会超时
    #     if len(nums)<2:
    #         return False
    #     sum_=0
    #     for i in range(len(nums)):
    #         sum_=nums[i]
    #         for j in range(i+1,len(nums)):
    #             sum_+=nums[j]
    #             if(k==0 and sum_==0) or (k!=0 and (sum_%k)==0):
    #                 return True
    #     return False

    # def checkSubarraySum(self, nums, k):
    #     #这种方法会把所有的情况遍历一遍,超时，因为，sum()函数每次都要重新计算一次，
    #     #可以把之前计算好的拿过来用，这样就不会超时了
    #     #外层以长度为循环，内层 从起始点开始循环
    #     size = len(nums)
    #     if size < 2:
    #         return False
    #
    #     for l in range(2, size + 1):
    #         for start in range(size - l + 1):
    #             sub = nums[start:start + l]
    #             sum_  = sum(sub)
    #             if not k:
    #                 if not sum_:return True
    #             else:
    #                 if sum_ %k == 0: return True
    #
    #     return False


class Solution:
    def checkSubarraySum(self, nums, k):
        size = len(nums)
        if size < 2:return False
        temp = 0
        lookup = {}
        #这是为了长度为2，且两个数均是k的倍数的情况考虑的；如果不这么做，两次取的下标分布为0，1，差值为1，无法得到结果
        #所以要把起始下标设为-1，这样当总长度为2时，才能得出正确结果
        lookup[0] = -1

        for i in range(size):
            temp += nums[i]
            if k:
                temp %= k
            pre = lookup.get(temp,None)
            if pre != None:
                if i - pre > 1:
                    return True
            else:
                lookup[temp] = i
        return False


if __name__ == '__main__':
    so = Solution()
    nums = [1,24,6] #[23,2,6,4,7] [23,2,6,4,7]

    k =6
    res = so.checkSubarraySum(nums,k)
    print(res)

