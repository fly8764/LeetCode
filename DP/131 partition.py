class Solution:
    # 动态规划，类似于 5. 最长回文子串，
    # 在这里，只有当两边相等，紧接着的内部是回文串时，dp[l][r] ==  True
    # 然后，依据dp来保存 对应的回文子串；这一步其实类似于 回溯法，这不过，这里使用
    # 动态规划 来记录状态，而不是 在回溯法中 每次都判断一次
    # 题解中的回溯法 判读回文串 很是干脆直接 s[:i] == s[:i][::-1]
    # def partition(self, s):
    #     if not s:
    #         return []
    #     size = len(s)
    #     dp = [[0]*size for _ in range(size)]
    #
    #     for r in range(size):
    #         for l in range(r+1):#这里 l可以和r相等，毕竟单个字符也是回文串
    #             if s[l] == s[r] and (r- l < 3 or dp[l+1][r-1]):
    #                 dp[l][r] = 1
    #             #这里不想 最长回文子串 那样，即使不相等，还要把子结构中的最长值记录
    #     res = []
    #     def find(l,temp):
    #         if l == size:
    #            res.append(temp)
    #         for r in range(l,size):
    #             if dp[l][r]:
    #                 find(r+1,temp + [s[l:r+1]])
    #     find(0,[])
    #     return res

    def __init__(self):
        self.res = []

    # def check(self,s):
    # 中心扩散法，相比与sub[:]==sub[:][::-1] 要麻烦一些
    #     size = len(s)
    #     left,right = 0,size-1
    #     while s[left] == s[right]:
    #         if right <= left:
    #             return True
    #         # if s[left] == s[right]:
    #         left += 1
    #         right -= 1
    #     return False
    #
    def dfs(self,s,cur):
        size = len(s)
        if not size:
            self.res.append(cur)
        #下面for循环中的 有边界 是 size+1,而不是 size，
        for i in range(1,size+1):
            sub = s[:i]
            if sub[:]==sub[:][::-1]:
                self.dfs(s[i:],cur +[sub])

    def partition(self, s):
        self.dfs(s,[])
        return self.res


if __name__ == '__main__':
    so = Solution()
    res = so.partition('aab')
    print(res)