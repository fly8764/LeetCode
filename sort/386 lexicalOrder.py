class Solution:
    def __init__(self):
        self.res = []

    def find(self,m,n):
        if m > n:
            return
        self.res.append(m)

        t = m*10
        for i in range(10):
            self.find(t+i,n)

    def lexicalOrder(self, n):
        res = []
        for i in range(1,10):
            self.find(i,n)
        return self.res

