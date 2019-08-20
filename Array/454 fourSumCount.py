class Solution:
    def fourSumCount(self, A, B, C, D):
        #不需要排序
        # A.sort()
        # B.sort()
        # C.sort()
        # D.sort()
        cnt = 0
        if not len(A) and not len(B) and not len(C) and not len(D):
            return cnt
        map = {}
        for i in range(len(C)):
            for j in range(len(D)):
               sub = C[i] + D[j]
               if sub not in map:
                   map[sub] = 1
               else:
                   map[sub] += 1

        for i in range((len(A))):
            for j in range(len(B)):
                temp = - A[i] - B[j]
                if temp not in map:continue
                cnt += map[temp]

        return cnt

if __name__ == '__main__':
    so = Solution()
    A = [1,2]
    B = [-2,-1]
    C = [-1,2]
    D = [0,2]
    res = so.fourSumCount(A,B,C,D)
    print(res)
