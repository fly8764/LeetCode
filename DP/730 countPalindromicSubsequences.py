class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        from collections import defaultdict
        import bisect
        M = 1000000007
        characters = defaultdict(list)
        for idx, s in enumerate(S):
            characters[s].append(idx)
        print(characters)
        lookup = {}

        def helper(i, j):
            if i >= j: return 0
            if (i, j) in lookup:
                return lookup[(i, j)]
            res = 0
            for c, v in characters.items():
                print(c, v)
                n = len(v)
                new_i = None
                idx_i = bisect.bisect_left(v, i)
                if idx_i < n:
                    new_i = v[idx_i]
                if new_i == None or new_i >= j:
                    continue
                idx_j = bisect.bisect_left(v, j) - 1
                new_j = v[idx_j]
                res += helper(new_i + 1, new_j) + 2 if new_i != new_j else 1
                #取余 满足 结合律
            lookup[(i, j)] = res % M
            # print(lookup)
            return lookup[(i, j)]

        return helper(0, len(S))

    # def countPalindromicSubsequences(self, S):
    #     if not S:
    #         return 0
    #     size = len(S)
    #     # dp = [[0]*size for _ in range(size)]
    #     # sub = [['']*size for _ in range(size)]
    #     res = []
    #
    #     for r in range(size):
    #         # dp[r][r] = 1
    #         # sub[r][r] = S[r]
    #         # res.append(sub[r][r])
    #         res.append(S[r])
    #         for l in range(r-1,-1,-1):
    #             if S[l] == S[r]:
    #                 res.append(S[l]+S[r])
    #                 # dp[l][r] = dp[l+1][r-1] + 2
    #                 cur = []
    #                 for i in range(len(res)):
    #                     cur.append(S[l] + res[i]+S[r])
    #                 res.extend(cur)
    #
    #             # else:
    #                 # dp[l][r] = max(dp[l+1][r],dp[l][r-1])
    #
    #                 # sub[l][r] = S[l]+sub[l+1][r-1] +S[r]
    #             # elif dp[l+1][r] > dp[l][r-1]:
    #             #     dp[l][r] = dp[l + 1][r]
    #             #     sub[l][r] = sub[l + 1][r]
    #             # elif dp[l+1][r] <= dp[l][r-1]:
    #             #     dp[l][r] = dp[l][r-1]
    #             #     sub[l][r] = sub[l][r-1]
    #             # res.add(sub[l][r])
    #
    #     return set(res)


if __name__ == "__main__":
    so = Solution()
    S = 'bccb'
    res = so.countPalindromicSubsequences(S)
    print(res)
    print(len(res))


