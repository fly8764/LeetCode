# -*- coding:utf-8 -*-
#19:30--20:11  41 mins
#方法一：T(n) = n
class Solution:
    def __init__(self):
        self.cnt = 0
        self.n = 0

    def dfs(self,m,cur):
        # m 是起始值
        for i in range(10):
            temp = m*10 + i
            if temp <= self.n and temp > 0:
                if i == 1:
                    self.cnt += cur + 1
                    self.dfs(temp,cur +1)
                else:
                    self.cnt += cur
                    self.dfs(temp, cur)
            elif temp > self.n:
                break

    def NumberOf1Between1AndN_Solution(self, n):
        self.n = n
        self.cnt = 0
        self.dfs(0,0)
        return self.cnt


if __name__== '__main__':
    so = Solution()
    res = so.NumberOf1Between1AndN_Solution(55)
    print(res)