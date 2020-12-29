'''
解法一 哈希表法
参照两数之和的题目，先计算两数之和，存到哈希表中，然后当作三数之和来计算，同样是哈希表法；
优点：不用排序，但是查表耗费时间。
T(n) = o(nlogn*n^2) nlogn是哈希表查表的时间复杂度
解法二 双指针法
先固定前两个数，在后两个数上使用双指针法；需要提前排序。
T(n) = o(n^3)
'''
class Solution1:
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

class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4:return []

        nums.sort()
        result = []
        if nums[0]*4 > target or nums[-1]*4 < target:return []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:continue
                p = j+1
                q = n-1
                res = target - nums[i] - nums[j]
                while p < q:
                    tmp = nums[p] + nums[q]
                    if tmp == res:
                        result.append([nums[i],nums[j],nums[p],nums[q]])
                        p += 1
                        while p < q and nums[p] == nums[p-1]:p += 1
                        q -= 1
                        while q > p and nums[q] == nums[q+1]:q -= 1
                    elif tmp < res:
                        p += 1
                        # print(p)
                        # 这里增加一个循环，反而会增加时间,不如不加了
                        # while p < q and nums[p] == nums[p-1]: p += 1
                    else:
                        q -= 1
                        # while p < q and nums[q] == nums[q+1]: q -= 1
        return result



if __name__ == '__main__':
    so = Solution()
    # nums,target = [1, 0, -1, 0, -2, 2],0
    nums,target = [-4,0,-4,2,2,2,-2,-2],7
    res = so.fourSum(nums,target)
    print(res)


