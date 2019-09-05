import functools


class Solution:
    def find(self,n):
        n += 5

    def test(self,n):
        self.find(n)
        print(n)
        return n

    def cmp(self,a, b):
        if b < a:
            return -1
        if a < b:
            return 1
        return 0

    def help(self,a):
        res = sorted(a, key=functools.cmp_to_key(self.cmp))
        return res




if __name__ == "__main__":
    so = Solution()
    a = [1, 2, 5, 4]
    res = so.help(a)
    print(res)
    # def cmp(a, b):
    #     if b < a:
    #         return -1
    #     if a < b:
    #         return 1
    #     return 0
    #
    #
    # a = [1, 2, 5, 4]
    # print(sorted(a, key=functools.cmp_to_key(cmp)))

