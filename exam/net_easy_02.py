class Solution():
    def find(self,a,b,p,q):
        target = b-a
        if p >= target:
            return 1
        temp = p
        cnt = 0
        while temp < target:
            cnt += 1
            temp *= q
        return cnt + 1

if __name__ == '__main__':
    t = int(input())
    so = Solution()
    while t:
        t -= 1
        line = list(map(int,input().split()))
        a,b,p,q = line[0],line[1],line[2],line[3]
        print(so.find(a,b,p,q))


