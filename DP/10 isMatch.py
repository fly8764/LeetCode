# 21:19--
class Solution:
    # 动态规划：(备忘录)递归
    def isMatch(self, s, p):
        memo = {}
        def dp(i,j):
            if (i,j) in memo: return memo[(i,j)]
            if j == len(p):return i == len(s)

            first = i < len(s) and p[j] in {s[i],'.'}

            if j <= len(p)-2 and p[j+1] == '*':
                ans = dp(i,j+2) or first and dp(i+1,j)
            else:
                ans = first and dp(i+1,j+1)

            memo[(i,j)] = ans
            return ans
        return dp(0,0)

if __name__ == '__main__':
    so = Solution()
    s = "aab"
    p = "c*a*b"
    res = so.isMatch(s,p)
    print(res)




