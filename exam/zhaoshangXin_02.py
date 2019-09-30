class Solution:
    def dfs(self,day):
        #这一天已经完成
        if self.state[day] == 1:return 0
        #这一天没有前置完成项，返回1
        if self.grid[day][0] == 0:
            return 1
        task = self.grid[day][1:]

        #完成day所需要的天数
        cnt = 1 #完成该天需要 1
        for item in task:
            cnt += self.dfs(item)
            self.state[item] = 1
        return cnt


    def find(self,n,grid):
        #这个grid要提前多加一行，为了和下面的保持一致
        self.grid = grid
        self.state = [0]*(n+1)
        self.res = [0]*(n+1)
        for i in range(1,1+n):
            if self.state[i] == 1:
                self.res[i] = 0
            else:
                self.res[i] = self.dfs(i)

        ret = list(map(str,self.res[1:]))
        ret = ' '.join(ret)

        # return self.res[1:]
        return ret


if __name__ == '__main__':
    n = int(input())
    t = n
    grid = [[]]
    while t:
        t -= 1
        line = list(map(int,input().split()))
        grid.append(line)
    so = Solution()
    res = so.find(n,grid)
    print(res)
    # for i in range(n-1):
    #     print(res[i],end=' ')
    # print(res[-1])
'''
3
1 2
0
1 2

2 0 1



5
2 3 5
1 4
2 2 5
0
1 4

5 0 0 0 0
'''




