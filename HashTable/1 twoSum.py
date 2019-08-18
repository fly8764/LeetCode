#哈希表(字典)，把已经出现的值，记录下来，下次需要时可以直接查看
class Solution:
    def twoSum(self, nums, target):
        #字典查值比较快
        temp = dict()
        for idx,value in enumerate(nums):
            if temp.get(target - value) is not None:
                return [temp.get(target - value),idx]
            temp[value] = idx