# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n == 0 or n == 1:
            return n
        else:
            a = 0
            b = 1
            i = 1
            while i < n:
                i += 1
                c = b
                b = b + a
                a = c
            return b

if __name__ == '__main__':
    func = Solution()
    print(func.Fibonacci(4))