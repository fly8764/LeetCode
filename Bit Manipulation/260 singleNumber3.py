class Solution1:
    def singleNumber(self, nums):
        #位运算  T(n) = n O(n) = l
        xor = 0
        res = [0,0]
        #1.将所有的值进行异或，找到两个异类的单值，
        # xor位上为1的 表示是这个单值异或的结果，表示 这两个单值在该位上不同
        #2.找到xor最右边为1的位 mask
        #3.将该位上为1 的分为一类，为0的分为一类，所有值异或，由于其他的都是成对
        #所以，异或后为零，最后每一类只剩下一个单值
        for num in nums:
            xor ^= num
        #找到xor 最右边的1 所在位，xor和其“补码”(前面取负号)与 操作
        mask = xor&(-xor)

        for num in nums:
            if num & mask == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res

    def singleNumber0(self, nums):
        # 哈希表(字典) T(n) = n O(n) = n
        arr = {}
        res = []
        for num in nums:
            if num not in arr:
                arr[num] = 1
            else:
                arr[num] += 1

        for key,value in arr.items():
            if value == 1:
                res.append(key)
        return res


'''
2020/12/13 15:38
方法一 位运算 异或
类似于136题的异或操作，把所有的数异或一次，这样会得到两个单独数的异或结果res。
然后找到res二进制中最右边的1所在的位置
法一：a^(-a)
法二：与和左移
a
mask = 1
while(mask&a == 0):
    mask <<= 1
'''

class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num

        single = [0,0]
        # 找到最右边的1位置
        mask = res&(-res)
        for num in nums:
            if mask & num == 0:
                single[0] ^= num
            else:
                single[1] ^= num

        return single





if __name__ == '__main__':
    so = Solution()
    res = so.singleNumber([1,2,1,3,2,5])
    print(res)
