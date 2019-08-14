class Solution:
    def __init__(self):
        self.res = []

    def check(self,s):
        size = len(s)
        left,right = 0,size-1
        while s[left] == s[right]:
            if right <= left:
                return True
            # if s[left] == s[right]:
            left += 1
            right -= 1
        return False

    def dfs(self,s,cur):
        size = len(s)
        if not size:
            self.res.append(cur)
        #下面for循环中的 有边界 是 size+1,而不是 size，
        for i in range(1,size+1):
            sub = s[:i]
            if self.check(sub):
                self.dfs(s[i:],cur +[sub])


    def partition(self, s):
        self.dfs(s,[])
        return self.res


if __name__ == '__main__':
    so = Solution()
    res = so.partition('aab')
    print(res)