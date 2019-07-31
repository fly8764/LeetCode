class Solution:
    def singleNumber(self, nums):
        #通用解法：数组中某数出现k次，k>=2，有一数出现一次，求出该数
        #负数会报错
        res = 0
        size = 32
        bit = [0]*size #前两位不用考虑 符号位 进制位

        for num in nums:
            r = 1
            for j in range(size-1,-1,-1): #这里要逆序，列表的最右边对应着最小位
                if num & r:
                    bit[j] += 1
                r <<= 1

        r = 1
        for j in range(size-1,-1,-1):
            if bit[j] % 3:
                res ^= r #取位
            r <<= 1

        return res


    def singleNumber1(self, nums):
        #使用二进制 来模拟 三进制 运算(不进位的加法)
        #上一题136 的异或运算是 二进制下不考虑进位的加法  0+0 = 0， 1+1=0……
        #可以通过某种运算$，使a $ a $ a = 0，0 $ a = a，
        # 即创建“三进制下不考虑进位的加法”

        #ones只记录当前 二进制只有一个 1 的那些位，twos 只记录当前二进制 只有两个 1
        #的位数， ones & twos 为1，则说明当前位1 的个数为 3 ，需要清零，a $ a $ a = 0
        # ones &= ~ threes 这种取反  再与的方式 把ones twos 对应位清零
        #ones twos 只关心局部，threes看全局，所以最后需要threes 来清零
        ones,twos,threes = 0,0,0
        for num in nums:
            twos |= ones&num #
            ones ^= num
            threes = ones & twos
            ones &= ~ threes
            twos &= ~ threes

        return ones



    def singleNumber0(self, nums):
        #1.使用set()去重后的数组求和 乘以 3，2.减去 原有数组求和 3.最后除以 2
        sum_ = sum(set(nums))
        return  (sum_ *3 - sum(nums))//2


if __name__== '__main__':
    so = Solution()
    res = so.singleNumber([0,1,0,1,0,1,99])
    print(res)

    res = so.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
    print(res)
