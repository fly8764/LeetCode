class Solution():
    def bfs(self,n,m,a,b,c):
        grid = [[0]*m for _ in range(n)]
        grid[a][b] = c

        if c< 1:return grid

        dir = [[-1,0],[1,0],[0,1],[0,-1]]
        point = [[a,b]]
        c -= 1
        temp = []
        while c and point:
            while point:
                p = point.pop(0)
                for item in dir:
                    new_x = p[0] + item[0]
                    new_y = p[1] + item[1]
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = c
                        temp.append([new_x, new_y])
            point.extend(temp)
            temp = []
            c -= 1
        return grid


if __name__ == '__main__':
    so = Solution()
    t = int(input())
    i = 1
    while t:
        t -= 1
        line = list(map(int,input().split()))
        n,m,a,b,c = line[0],line[1],line[2],line[3],line[4]

        res = so.bfs(n,m,a,b,c)
        print('Case #%d:'%i)
        i += 1
        for j in range(n):
            nums = list(map(str,res[j]))
            print(' '.join(nums))

