class Solution:
    # def __init__(self):
    #     self.res = []
    #
    # def find(self,m,n):
    #     if m > n:
    #         return
    #     self.res.append(m)
    #
    #     t = m*10
    #     for i in range(10):
    #         self.find(t+i,n)
    #
    # def lexicalOrder(self, n):
    #     res = []
    #     for i in range(1,10):
    #         self.find(i,n)
    #     return self.res

    def __init__(self):
        self.res = []
        self.n = 0

    def dfs(self,temp):
        for i in range(10):
            ans = temp*10 + i
            if ans <= self.n:
                if ans > 0:
                    self.res.append(ans)
                    self.dfs(ans)
            else:return

    def lexicalOrder(self, n):
        self.n = n
        self.dfs(0)
        return self.res

if __name__ == '__main__':
    so = Solution()
    res = so.lexicalOrder(13)
    print(res)


