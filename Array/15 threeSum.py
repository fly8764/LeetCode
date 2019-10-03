'''
方法一：排序、双指针
数组排序，然后左右指针向中间移动，根据 和与目标值的大小来判断左右指针的移动情况
双指针的前提：有序数组，所以要先 排序，注意排除相同值的情况，左移或者右移后，
如果和上次的相同，则再移动一次
区别：这种方法不能直接返回对应值的原始下标，

方法二：类似于两数之和
把遇到的数存在字典里，每次先询问 另一个值是否存在，若存在，则返回结果；否则把新值存在字典里
这种方法 不排序，所以没法使用双指针，在查找时，会耽误一些时间，所以没有方法一快
区别：这种方法能直接返回对应值的原始下标，
'''
class Solution:
    def threeSum(self, nums):
        size = len(nums)
        if size <3:return []
        nums.sort()
        res = []
        for k in range(size-2):
            if nums[k] > 0:break
            if k >0 and nums[k] == nums[k-1]:continue #这个细节非常重要
            i,j  = k+1,size-1 #两边同时向中间移动(双指针)
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s == 0:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:j -= 1
                elif s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:i += 1
                else:#注意这个else 和前面的elif 对齐，说明是一个级别的
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:j -= 1
        return res


if __name__ == '__main__':
    so = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = so.threeSum(nums)
    print(res)