class Solution:
    def twoSum(self, nums, target):
        # 字典查值比较快
        temp = dict()
        for idx,value in enumerate(nums):
            if temp.get(target - value) is not None:
            # if temp.get(target - value):
                #这种不适用 is not None的，当 temp.get()返回的是 0 时就出问题了
            # if temp[target - value] :
                return [temp.get(target - value),idx]
            temp[value] = idx

    def twoSum0(self, nums, target):
        #暴力法
        size = len(nums)
        for i in range(size-1):
            for j in range(i+1,size):
                if nums[j] + nums[i] == target:
                    return [i,j]

if __name__ == '__main__':
    so = Solution()
    # nums = [2, 7, 11, 15]
    nums = [2,7,11,15]
    target = 9
    res = so.twoSum(nums,target)
    print(res)


