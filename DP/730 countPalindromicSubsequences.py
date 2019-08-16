class Solution:
    def countPalindromicSubsequences(self, S):
        if not S:
            return 0
        size = len(S)
        dp = [[0]*size for _ in range(size)]
        sub = [['']*size for _ in range(size)]
        res = set()

        for r in range(size):
            dp[r][r] = 1
            sub[r][r] = S[r]
            res.add(sub[r][r])
            for l in range(r-1,-1,-1):
                if S[l] == S[r]:
                    res.add(S[l]+S[r])
                    dp[l][r] = dp[l+1][r-1] + 2

                    sub[l][r] = S[l]+sub[l+1][r-1] +S[r]
                elif dp[l+1][r] > dp[l][r-1]:
                    dp[l][r] = dp[l + 1][r]
                    sub[l][r] = sub[l + 1][r]
                elif dp[l+1][r] <= dp[l][r-1]:
                    dp[l][r] = dp[l][r-1]
                    sub[l][r] = sub[l][r-1]
                res.add(sub[l][r])

        return res


if __name__ == "__main__":
    so = Solution()
    S = 'bccb'
    res = so.countPalindromicSubsequences(S)
    print(res)
    print(len(res))


