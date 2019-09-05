class Solution():
    #暴力递归 超时
    def __init__(self):
        self.target = 0
        self.flag = 0

    def dfs(self,nums,cur):
        if cur == self.target:
            self.flag = 1
            return

        size = len(nums)
        if not size:
            return

        for i in range(size):
            if self.flag :return
            if cur+nums[i] < self.target:
                self.dfs(nums[:i] + nums[i + 1:], cur + nums[i])
                if self.flag: return
                self.dfs(nums[:i] + nums[i + 1:], cur)
            else:
                break


    def find(self,nums,target):
        self.target = target
        self.dfs(nums,0)
        return self.flag


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    target = int(input())
    so = Solution()
    nums.sort()
    res = so.find(nums,target)
    print(res)



