class Solution1():
    def __init__(self):
        pass

    def maxSubArray(self,nums):
        length = len(nums)
        if length== 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0:length//2])
            max_right = self.maxSubArray(nums[length//2:])

        temp_l = 0
        max_tmp_l = nums[length//2-1]
        for i in range(length//2-1,-1,-1):
            temp_l += nums[i]
            max_tmp_l = max(max_tmp_l,temp_l)

        tmp_r = 0
        max_tmp_r = nums[length//2]
        for j in range(length//2,length):
            tmp_r += nums[j]
            max_tmp_r = max(max_tmp_r,tmp_r)

        tmp = max_tmp_l+ max_tmp_r

        return max(max_left,max_right,tmp)



    def maxSubArray1(self, nums):
        pass
        temp = nums[0]
        max_ = temp

        for i in range(1, len(nums)):
            if temp > 0:
                temp += nums[i]

            else:
                temp = nums[i]
            max_ = max(temp, max_)

        return max_

'''
这里 sum>0，整数增益的原理是一种遍历方式，
遍历有三种方式，
1.以每个节点为起点的子序列；
2.各种长度下的子序列，最长回文串用到；
3.以每个节点为尾节点的子序列，这题用到的就是这种方式，
在计算每个节点是i，判读是否要接上 以上一个节点为尾节点的子序列 dp[i-1];
如果dp[i-1]>0,则对子序列和有益，拼接上 dp[i] = dp[i-1]+nums[i];
dp[i-1]<=0,对结果无益，不接，dp[i] = nums[i]，
这样，每个节点都考虑到了，最终取max(dp),
由于每次判断完一个节点后，都会判断当前的最大值dp[i]和maxx的大小；
所以，最终可以简化，仅仅使用两个标量即可，就形成了“正数增益”的方法。

'''
class Solution:
    def maxSubArray(self, nums):
        #二分法 把数组分为左右两半，最终结果可能出现的三种情况 T(n) = nlogn
        #左边、右边、左边一部分+右边一部分
        #其中第三种情况，在求左边时，要从右往左遍历，求右边时要从左往右遍历
        size = len(nums)
        if size == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[:size//2])
            max_right = self.maxSubArray(nums[size//2:])
        max_l = nums[size//2-1]
        temp = 0
        for i in range(size//2-1,-1,-1):
            temp += nums[i]
            max_l = max(max_l,temp)

        max_r = nums[size//2]
        temp = 0
        for i in range(size//2,size):
            temp += nums[i]
            max_r = max(max_r,temp)
        return max(max_left,max_right,max_l+max_r)

    # def maxSubArray(self, nums):
    # T(n) = n   O(n) = o(l)
    #     temp = nums[0]
    #     maxx = temp
    #     for i in range(1,len(nums)):
    #         if temp > 0:
    #             temp += nums[i]
    #         else:
    #             temp = nums[i]
    #         maxx = max(maxx,temp)
    #     return maxx

    # def maxSubArray(self, nums):
    # T(n) = n   O(n) = o(n)
    #     size = len(nums)
    #     if size < 1:return 0
    #     dp = [0]*size
    #     dp[0] = nums[0]
    #     for i in range(1,size):
    #         dp[i] = max(dp[i-1]+nums[i],nums[i])
    #     return max(dp)



if __name__ == '__main__':
    so = Solution()
    res = so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)