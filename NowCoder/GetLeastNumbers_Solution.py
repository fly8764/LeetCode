# -*- coding:utf-8 -*-
#堆排序 比较慢 T(n)=nlogn
#快排
class Solution:
    def __init__(self):
        self.size = 0
        self.k = 0

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

    def partiton(self,nums,s,t):
        temp = nums[s]
        index = s+1
        if s < t:
            for i in range(s+1,t+1):
                if nums[i] < temp:
                    self.swap(nums,i,index)
                    index += 1
            self.swap(nums,s,index-1)
        return index - 1

    def quickSort(self,nums,s,t):
        if s == t:return
        elif s < t:
            pivot = self.partiton(nums,s,t)
            self.quickSort(nums, s, pivot - 1)
            self.quickSort(nums, pivot + 1, t)

        #不要把partition写在里面，不然变量的作用范围容易受到影响；
        #最好写在外面
        # temp = nums[s]
        # index = s+1
        # if s < t:
        #     for i in range(s+1,t+1):
        #         if nums[i] < temp:
        #             self.swap(nums,i,index)
        #             index += 1
        #     self.swap(nums,s,index-1)
        #
        # pviot = index - 1
        # self.quickSort(nums,s,pviot-1)
        # self.quickSort(nums,pviot+1,t)

    def GetLeastNumbers_Solution(self, nums, k):
        #剑指offer上的解法一 牛客网超时
        if nums == [] or len(nums) < k:return []
        s = 0
        end = len(nums) -1
        index = self.partiton(nums,s,end)
        while index != k -1:
            if index < k-1:
                s = index +1
                index = self.partiton(nums,s,end)
            else:
                end = index - 1
                index = self.partiton(nums,s,end)

        return nums[:k]




if __name__ == '__main__':
    so = Solution()
    nums = [4,5,1,6,2,7,3,8]
    k = 4
    res = so.GetLeastNumbers_Solution(nums,k)
    print(res)
    # so.quickSort(nums,0,len(nums)-1)
    # print(nums)