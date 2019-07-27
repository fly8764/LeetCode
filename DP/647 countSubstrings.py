class Solution:
    def countSubstrings(self, s):
        size = len(s)
        if size < 2:
            return size
        # 中心扩散法

    def countSubstrings2(self, s):
        size = len(s)
        if size < 2:
            return size

        res = 0
        for i in range(size):
            res += self.center(s, size, i, i)
            res += self.center(s, size, i, i + 1)

        return res

    def center(self, s, size, left, right):
        res = 0
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1
            right += 1
            res += 1

        return res

    #动态规划
    def countSubstrings1(self, s):
        size = len(s)
        if size < 2:
            return size

        dp = [[False for _ in range(size)] for _ in range(size)]
        res = size

        for r in range(1, size):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    res += 1

        return res


if __name__ == '__main__':
    so = Solution()
    res = so.countSubstrings('aaa')
    print(res)