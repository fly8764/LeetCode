class Solution:
    def findOrder(self, n, pre):
        ind = [0]*n
        edge = {}
        q = []
        res = []
        for item in pre:
            if item[1] not in edge:
                edge[item[1]] = [item[0]]
            else:
                edge[item[1]].append(item[0])
            ind[item[0]] += 1

        for i in range(n):
            if ind[i] == 0:
                q.append(i)

        while q:
            p = q.pop()
            res.append(p)
            if p in edge:
                for tq in edge[p]:
                    ind[tq] -= 1
                    if ind[tq] == 0:
                        q.append(tq)
        if len(res) == n:
            return res
        else:
            return []

if __name__ == "__main__":
    so = Solution()
    n = 2
    # pre = [[1,0],[2,0],[3,1],[3,2]]
    pre = [[1,0]]
    res = so.findOrder(n,pre)
    print(res)
