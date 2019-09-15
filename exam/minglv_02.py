class Solution:
    def jumpFloor(self, n):
        a = 1
        b = 2
        if n == 1:
            return a
        if n == 2:
            return b
        for  i in range(n-2):
            c = a + b
            a = b
            b = c
        return b


if __name__ == '__main__':
    n = int(input())
    so = Solution()
    res = so.jumpFloor(n)
    print(res)