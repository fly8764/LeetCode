class Solution:
    def insetSort(self,nums):
        #T(n) = n**2
        #从前往后遍历
        size = len(nums)
        if size < 2:
            return nums

        for i in range(1,size):
            j = i-1
            temp = nums[i]
            #扫描，从后往前扫描
            while j > -1 and nums[j] > temp:
                nums[j+1] = nums[j] #较大值往后挪
                j -= 1
            nums[j+1] = temp

        return nums

    def shellSort(self,nums):
        #T(n) = n*logn
        # 实际遍历时，不是 在一定间隔下，把一个子序列简单插入排序后，再对下一个子序列排序
        # 而是 把所有的从前(nums[d])到后逐元素的进行，排序时找到前面间隔d的元素比较
        # 一种子序列拍完了
        size = len(nums)
        if size < 2:
            return nums
        d = size//2
        while d > 0:
            for i in range(d,size):
                temp = nums[i]
                j = i - d
                while j > -1 and nums[j] > temp:
                #这里注意 nums[j] > temp而不是 nums[j]> nums[j+d](下面第一行会更行nums[j+d])
                    nums[j+d] = nums[j]
                    j -= d
                nums[j+d] = temp
            d //= 2
        return nums

    def bubbleSort(self,nums):
        #T(n) = n**2
        size = len(nums)
        if size < 2:return nums
        for i in range(1,size):
            for j in range(i-1,-1,-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        return nums

    # def quickSort(self,nums):
        #递归
        #方法一：开辟新的数组
        # size = len(nums)
        # if size < 2:return nums
        # temp = nums[0]
        # left_sub = []
        # right_sub = []
        #
        # for i in range(1,size):
        #     if nums[i] < temp:
        #         left_sub.append(nums[i])
        #     else:
        #         right_sub.append(nums[i])
        # left = self.quickSort(left_sub)
        # right = self.quickSort(right_sub)
        # return left+[temp] + right
    # def quickSort(self,nums,s,t):
    #     left = s
    #     right = t
    #     if s < t:
    #         temp = nums[s]
    #         while left < right: #从两边往中间扫描，直到left == right
    #             while right > left and nums[right] > temp:
    #                 right -= 1
    #             if left < right: #先不管 nums[left]的大小如何，先交换到右边的nums[right]再说，到那边再比较
    #                 tmp = nums[left]
    #                 nums[left] = nums[right]
    #                 nums[right] = tmp
    #                 left += 1
    #             while left < right and nums[left] < temp:
    #                 left += 1
    #             if left < right:#先不管 nums[right]的大小如何，先交换到左边的nums[left]再说，到那边再比较
    #                 tmp = nums[right]
    #                 nums[right] = nums[left]
    #                 nums[left] = tmp
    #                 right -= 1
    #         nums[left] = temp
    #         self.quickSort(nums,s,left-1)
    #         self.quickSort(nums,left+1,t)

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def partition(self,nums,s,t):
        #从左往右逐个扫描，而不是像上面那个解法，左右两边同时向中间扫描，直到相等
        pivot = s
        index = pivot + 1
        temp = nums[pivot]
        for i in range(pivot+1,t+1):
            if nums[i] < temp:
                self.swap(nums,i,index)
                index += 1
        self.swap(nums,pivot,index-1)
        return index - 1

    def quickSort(self,nums,s,t):
        if s == t:return nums
        elif s < t:
            pivot = self.partition(nums, s, t)
            self.quickSort(nums, s, pivot - 1)
            self.quickSort(nums, pivot + 1, t)

    def selectSort(self,nums):
        #类似于冒泡排序，只不过，是在找到未排列 列表中的最小元素与 表头元素交换
        size = len(nums)

    def mergeSort(self,nums):
        #递归,从上到下 递归，从下到上返回；
        #递归题目：先假设 递归函数存在，拿过来直接用；然后，考虑如何处理边界情况
        size = len(nums)
        if size < 2:return nums
        mid = size//2
        left = nums[:mid]
        right = nums[mid:]
        return self.merge(self.mergeSort(left),self.mergeSort(right))

    def merge(self,left,right):
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        while left:
            res.append(left.pop(0))
        while right:
            res.append(right.pop(0))
        return res














if __name__ == '__main__':
    so = Solution()
    nums = [4,1,5,3,8,10,28,2]
    print(nums)
    print(sorted(nums),'gt')
    # res = so.insetSort(nums[:])
    # print(res)
    # res2 = so.shellSort(nums[:])
    # print(res2)
    # res3 = so.bubbleSort(nums[:])
    # print(res3,'bubbleSort')
    # so.quickSort(nums,0,len(nums)-1)
    # print(nums)
    res = so.mergeSort(nums)
    print(res)