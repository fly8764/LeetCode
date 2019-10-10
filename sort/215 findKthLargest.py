'''
使用分治法，T(n) = n O(n) = o(l)
基于快排的思想，pivot左边的元素都小于等于pivot，右边的都大于等于pivot
这样pivot的下标i就对应着第i+1小元素，
要找到第k大元素，其下标对应者 len - k +1 -1 = len-k(下标从0开始）
列表具有指针性质，如果直接带入函数中，函数会改变数组
'''
class Solution(object):
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def partition(self,nums,left,right):
        if right == left:
            return left
        pivot = nums[left]
        # j 代表当前小于pivot的数组的右边界
        j = left
        #这里for循环的右边界要包括right，所有是right+1
        for i in range(left+1,right+1):
            if nums[i] < pivot:#直接用小于就行了，不需要小于等于
                j += 1
                self.swap(nums,j,i)
        #这一步别忘了
        self.swap(nums,left,j)
        return j

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target = len(nums)- k
        left,right = 0,len(nums)-1
        while True:
            idx = self.partition(nums,left,right)
            if idx == target:
                return nums[target]
            #下面的下标都加1或者减1，因为下标对应的值已经算过，不用再算了
            elif idx < target:
                left = idx + 1
            else:
                right = idx -1


if __name__ == '__main__':
    so = Solution()
    print(so.findKthLargest( [3,2,1,5,6,4],k = 2))
    print(so.findKthLargest([3,2,3,1,2,4,5,5,6],k = 4))


