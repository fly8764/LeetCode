import itertools


class Solution:
    def combine(self, n, k):
        if n <1 or k>n or k<0:
            return []
        res = []
        def dfs(start,k,n,pre,res):
            if len(pre) == k:
                res.append(pre[:])
                return

            for i in range(start,n+2-k+len(pre)):
                pre.append(i)
                dfs(i+1,k,n,pre,res)
                pre.pop()
        dfs(1,k,n,[],res)
        return res



    def combine2(self, n, k):
        res = []

        def backtrack(i,k,tmp):
            if k == 0:
                res.append(tmp)
                return

            for idx in range(i,n+1):
                backtrack(idx+1,k-1,tmp+[idx])
        backtrack(1,k,[])

        return res

    def combine1(self, n, k):
        return list(itertools.combinations(range(1, n + 1), k))


if __name__ == '__main__':
    so = Solution()
    res = so.combine(4,2)
    print(res)
