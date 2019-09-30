class Solution:
    def dfs(self,grid):
        pass

    def search(self,nums):
        for i in range(len(nums)-1):
            if not self.state[i]:
                if nums[i] > nums[i+1]:
                    return i
        return len(nums) -1



    def find(self,n,m,grid):
        water = 0
        city = 0
        self.state = [[0]*m for _ in range(n)]

        while water < n or city < n*m:
            pass




if __name__ =='__main__':
    so = Solution()
    line = list(map(int,input().split()))
    n,m = line[0],line[1]
    grid = []
    t = n
    while t:
        t -= 1
        grid.append(list(map(int,input().split())))
