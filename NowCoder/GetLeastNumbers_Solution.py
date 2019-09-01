# -*- coding:utf-8 -*-
#堆排序 比较慢 T(n)=nlogn
#快排
class Solution:
    def __init__(self):
        self.size = 0

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def buildMinHeapify(self,nums):
        if self.size < 2:return

        for i in range(self.size//2,-1,-1):
            self.heapify(nums, i)

    def heapify(self,nums,i):
        least = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < self.size and nums[left] < nums[least]:
            least = left
        if right < self.size and nums[right] < nums[least]:
            least = right
        if least != i:
            self.swap(nums, least, i)
            self.heapify(nums, least)

    # def GetLeastNumbers_Solution(self, nums, k):
    #     # T(n) = (n/2)logn + klogn
    #     # 最下堆 排序
    #     # 注意 边界条件
    #     self.size = len(nums)
    #     if k > self.size or nums == []:return []
    #     self.buildMinHeapify(nums)
    #     res = []
    #     while k:
    #         k -= 1
    #         res.append(nums[0])
    #         self.swap(nums,0,self.size-1)
    #         self.size -= 1
    #         self.heapify(nums,0)
    #     return res

    def GetLeastNumbers_Solution(self, nums, k):
        pass


if __name__ == '__main__':
    so = Solution()
    nums = [4,5,1,6,2,7,3,8]
    k = 4
    res = so.GetLeastNumbers_Solution(nums,k)
    print(res)