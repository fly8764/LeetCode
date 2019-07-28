class Solution:
    def isUgly(self, num):
        #1是丑数；特例
        if num < 1:
            return False
        while num != 1:
            if num % 2 == 0:
                num /= 2
                continue
            if num % 3 == 0:
                num /= 3
                continue
            if num % 5 == 0:
                num /= 5
                continue
            return False
        return True

if __name__ == '__main__':
    so = Solution()
    res = so.isUgly(6)
    print(res)

    res = so.isUgly(8)
    print(res)

    res = so.isUgly(14)
    print(res)
