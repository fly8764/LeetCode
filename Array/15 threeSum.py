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
但是这种方法貌似行不通！！！
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
'''
这个题目做第二遍还是不会，花费了很多时间。
注意点：
1.重复值：在每次移动指针的时，判断和上一次的是否相同，相同再次滑动；
2.排序：有时为了简便快捷，更有规律性，可以先排序；特别时本题，需要去重，
  排序后能够有效的去重；
3.下面两个情况非常重要，
  大于零：因为之前进行了排序，所以当第一个值大于零时，中断。
  去重：未来防止出现重复的情况，要考虑移动后的情况和上一次是否相同。
'''
class Solution2:
    def threeSum2(self, nums):
        n = len(nums)
        if n < 3:return []
        result = []
        for i in range(n-2):
            first = nums[i]
            # dic = {first:i}
            dic = {}
            # 这一步非常重要，把包含first的情况都去除了，最终的结果中不会出现重复的情况。
            # 重复情况：tmp_array = nums[:i] + nums[i+1:]
            # 但是这种不能保证后面出现和first同值的情况，同值时结果依然不对。
            tmp_array = nums[i+1:]
            for j,num in enumerate(tmp_array):
                if -first - num in dic:
                    result.append([first,nums[j],-first - nums[j]])
                dic[num] = j
        return result

    def threeSum(self, nums):
        n = len(nums)
        if n < 3: return []
        result = []

        nums.sort()
        for i in range(n-2):
            first = nums[i]
            # 下面两个情况非常重要，
            # 大于零：因为之前进行了排序，所以当第一个值大于零时，中断。
            # 去重：未来防止出现重复的情况，要考虑移动后的情况和上一次是否相同。
            if first > 0:break
            # if i > 0 and nums[i] == nums[i-1]:continue
            target = -first
            j = i+1
            k = n-1
            while j < k:
                tmp = nums[j]+ nums[k]
                if tmp < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:j += 1
                elif tmp > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:k -= 1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]: k -= 1

        return result


if __name__ == '__main__':
    so = Solution2()
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-1, 0, 1]
    nums = [-1,0,1,2,-1,-4]
    # nums = [0,0,0,0]
    res = so.threeSum(nums)
    print(res)