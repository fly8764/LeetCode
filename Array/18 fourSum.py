class Solution:
    def fourSum(self, nums, target):
        size = len(nums)
        nums.sort()
        res = []
        if size < 4 or nums[0]*4 > target or nums[-1]*4 < target:
            return res

        map = {}
        for i in range(size-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,size):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                sub = nums[i] + nums[j]
                if sub not in map:
                    map[sub] = [[i,j]]
                else:
                    map[sub].append([i,j])


        for i in range(size- 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,size -2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                temp = target - nums[i] - nums[j]
                if temp not in map:
                    continue
                else:
                    for item in map[temp]:
                        if item[0] > j:
                            res.append([nums[i],nums[j],nums[item[0]],nums[item[1]]])
        return res



if __name__ == '__main__':
    so = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    res = so.fourSum(nums,target)
    print(res)


