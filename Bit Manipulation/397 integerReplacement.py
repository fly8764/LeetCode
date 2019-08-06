class Solution:
    def integerReplacement(self, n):
        #位运算(比较有技巧性) 是偶数直接除以2
        #奇数 减一 再除以2之后如何是偶数，则减一；或者特例，这个奇数是3
        #奇数 如果减一 再除以2之后，还是奇数，在加一
        #关键是 这个奇数的处理，发现上面的规律
        cnt = 0
        if n == 1:
            return 0

        while n > 1:
            if n & 1 == 0:
                n >>= 1
            else:
                if (n-1)//2 & 1 == 0 or n == 3:
                    n -= 1
                else:
                    n += 1
            cnt += 1

        return cnt


    def integerReplacement0(self, n):
        #递归
        if n == 1:
            return 0
        else:
            if n%2 == 0:
                return 1+self.integerReplacement(n//2)
            else:
                return 1+min(self.integerReplacement(n-1),self.integerReplacement(n+1))



if __name__ == '__main__':
    so = Solution()
    ret = so.integerReplacement(7)
    print(ret)
