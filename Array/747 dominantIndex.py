'''
方法一：暴力
先遍历一次，找到最大值，然后再遍历一次，判读是否符合要求，T(n) = nlogn
方法二：最大值，第二大值
最大值maxx和第二大值sec_max，如果满足要求，maxx对于其他的任意值都符合要求
一次遍历，找到两个值，最后判断一下；
方法三：最大值
从左到右遍历一次，遇到更大的值就更新最大值，同时判断新最大值是否大于旧最大值的两倍
如果没有更新最大值，则要判读当前的最大值是否新值的两倍，技巧：在这种情况下，如果已经有
不符合情况的，则不用再判断力；但是当出现更大的最大值时，要重新判断
'''
class Solution:
    def dominantIndex(self, nums):
        size = len(nums)
        if size < 1:return -1
        if size < 2:return 0

        second = 0
        maxx = nums[0]
        idx = 0
        for i in range(1,size):
            if nums[i] > maxx:
                second = maxx
                maxx = nums[i]
                idx = i
            else:
                if nums[i] > second:
                    second = nums[i]
        if maxx >= 2*second:
            return idx
        else:
            return -1


if __name__ == "__main__":
    so = Solution()
    print(so.dominantIndex([0,0,1,2]))