class Solution:

    def fourSum(self, nums, target):
        size = len(nums)
        # nums.sort()
        res = []
        # if size < 4 or nums[0]*4 > target or nums[-1]*4 < target:
        if size < 4 or min(nums)*4 > target or max(nums)*4 < target:
            return res

        map = {}

        #这里有个需要注意的地方，排序后，多个位置可能同值，此时，就要注意 求 哈希表的顺序
        #如果 最后 遍历是从左往右遍历的，则求哈希表时，应从右往左遍历，这样，对应同值不同位置，会先取到右边位置的，
        #由于 哈希表中的 和要满足位置上在 最后循环的值的右边，所有 当同值取靠右边的值时，可以 更容易满足要求，不会漏情况
        for i in range(size-1,0,-1):
            if i < size-1 and nums[i] == nums[i+1]:
                continue
            for j in range(i-1,-1,-1):
                if j < i-1 and nums[j] == nums[j+1]:
                    continue
                sub = nums[i]+ nums[j]
                if sub not in map:
                    map[sub] = [[j,i]]
                else:
                    map[sub].append([j,i])
        # map1 = {}
        # # 方向错误的 哈希表
        # for i in range(size-1):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i+1,size):
        #         if j > i+1 and nums[j] == nums[j-1]:
        #             continue
        #         sub = nums[i] + nums[j]
        #         if sub not in map1:
        #             map1[sub] = [[i,j]]
        #         else:
        #             map1[sub].append([i,j])

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


