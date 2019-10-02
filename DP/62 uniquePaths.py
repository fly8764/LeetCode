class Solution:
    def uniquePaths(self, m: int, n: int):
        cur = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j] += cur[j-1]
        return cur[-1]

class Solution1:
    def uniquePaths(self, m, n):
        pass


if __name__ == '__main__':
    so = Solution()
    res = so.uniquePaths(7,3)
    print(res)