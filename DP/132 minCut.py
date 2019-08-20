class Solution:
    def minCut(self, s):
        size = len(s)
        if not size:
            return 0

        dp = [float('inf')]*size
        dp[0] = 1

        for i in range(1,size):
            for j in range(1,i):
                sub = s[j+1:i+1]
                if sub[::] == sub[::-1]:
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[-1]

if __name__ == '__main__':
    so = Solution()
    s = 'aab'
    res = so.minCut(s)
    print(res)



