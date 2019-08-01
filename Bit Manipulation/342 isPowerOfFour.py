class Solution:
    def isPowerOfFour(self, n):
        #1.4的幂 最高位的1 都在奇数位上，所以判断最高位的1是否在奇数位，
        #2.或者奇数位只有一个1
        #1.0x5 0101 &(0100)(4)== 0100(num) 判断奇数位上的1
        #2.16进制 a：1010 都在偶数位上，(0100)(4)&(1010)(a)== 0 表示在奇数位上
        #0xaaaaaaaa&n == 0
        # return n > 0 and not n&(n-1) and n&(0x55555555) == n
        return n > 0 and not n&(n-1) and n&(0xaaaaaaaa) == 0



    def isPowerOfFour0(self, n):
        #4的幂 是1 左移 2n位的结果，
        if  n & (n-1):
            return False

        temp = 1
        while temp < n:
            temp <<= 2
        if temp == n:
            return True
        else:
            return False

if __name__ == "__main__":
    so = Solution()
    res = so.isPowerOfFour(16)
    print(res)
