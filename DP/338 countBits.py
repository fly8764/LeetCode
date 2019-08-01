class Solution:
    def countBits0(self, num):
        # 记忆查表，动态规划，根据已经计算出来的结果来计算当前的结果，同时注意末尾，奇1 偶0
        res = [0]*(num+1)
        res[0] = 0
        for i in range(1,num+1):
            res[i] = res[i>>1]+(i&1)
        return res

    def countBits(self, num):
        # 1.奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。
        # 2.偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。右移一位
        res = [0]*(num + 1)
        res[0] = 0
        for i in range(num+1):
            if i % 2 == 0:
                res[i] = res[i//2]
            else:
                res[i] = res[i-1]+1
        return res


if __name__ == '__main__':
    so = Solution()
    res = so.countBits0(5)
    print(res)
