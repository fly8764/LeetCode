class Solution:
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def bubbleSort(self,nums):
        #稳定排序法，相等大小的值 前后顺序不会改变
        #找最大值，放在未排序数组的后面
        #最坏情况,即倒序有序，T(n) = n*n
        #最好情况，正序有序，T(n) = n
        #这里的时间复杂度 是执行 swap的次数，而不是几层for循环的累乘
        size = len(nums)
        if size < 2:return nums
        for i in range(size):
            for j in range(size-1-i):
                if nums[j] > nums[j+1]:
                    self.swap(nums,j,j+1)

    def bubbleSort2(self, nums):
        #找最小值，把它放在最前面
        size = len(nums)
        if size < 2:return
        for i in range(size-1):
            for j in range(size-1,i,-1):
                if nums[j] < nums[j-1]:
                    self.swap(nums,j,j-1)

    def quickSort(self,nums,s,t):
        #不稳定，相等值的数字前后顺序可能变化
        #平均和最好：T(n) = nlogn
        #倒序有序时，就变成了冒泡排序，
        # 每次找到最大值，放在未排序数组的最后面，T(n) = n*2
        temp = nums[s]
        i,j = s,t
        if s < t:
            while i != j:
                while j > i and nums[j] > temp:
                    j -= 1
                if j > i:
                    self.swap(nums, i, j)
                    i += 1
                while i < j and nums[i] < temp:
                    i += 1
                if i < j:
                    self.swap(nums, i, j)
                    j -= 1
            #方法一：在while循环中排序时，如果采用每次需要调整位置时，都交换，
            #就是在始终调整 pivot的位置，所以就不需要在最后，再把i和其实点再交换一次了
            #这种方式，每次被甩到另一边的值是 pivot，相当于占个位置，下次另一边需要pivot这边交换时
            #直接和pivot交换即可；
            # 方法二：执行下面这条语句
            #每次遇到要交换的值nums[left]时，直接把它赋值到另一边，原来的位置left相当于占个坑，
            #在右边循环，遇到小于pivot的情况时nums[right]，再把nums[right]赋值到nums[left],
            # 同时，自己nums[right]相当于占个坑，为下一个交换过来的值准备,
            #最后，剩下的位置nums[i]留给pivot，即temp
            #nums[i] = temp

            self.quickSort(nums,s,i-1)
            self.quickSort(nums,i+1,t)

    def quickSort2(self,nums,s,t):
        temp = nums[s]
        i,j = s,t
        if s > t:
            return

        while i != j:
            while j > i and nums[j] > temp:
                j -= 1
            if j > i:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] < temp:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = temp
        self.quickSort(nums, s, i - 1)
        self.quickSort(nums, i + 1, t)

    def buildMaxHeap(self,nums):
        if self.size < 2:return
        #从倒数第二层开始调整堆
        for i in range(self.size//2,-1,-1):
            self.heapify(nums,i)

    def heapify(self,nums,i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        if left < self.size and nums[largest] < nums[left]:
            largest = left
        if right < self.size and nums[largest] < nums[right]:
            largest = right
        #这个条件别忘了
        if largest != i:
            self.swap(nums, largest, i)
            # 继续递归 调整堆，使得子树也满足最大堆的性质
            self.heapify(nums, largest)

    def heapSort(self,nums):
        #T(n) = nlogn
        #不断地调整堆，不稳定排序
        self.size = len(nums)
        self.buildMaxHeap(nums)
        #这里range到达 1即可，剩下一个值就是最小的
        for i in range(self.size-1,0,-1):
            self.swap(nums, 0, i)
            self.size -= 1
            self.heapify(nums,0)

    def mergeSort(self,nums):
        #稳定排序
        #T(n) = nlogn,无论最好，最坏都是
        size = len(nums)
        if size < 2:return nums

        left = self.mergeSort(nums[:size//2])
        right = self.mergeSort(nums[size//2:])
        res = []
        #这种写法不好
        # l = left.pop(0)
        # r = right.pop(0)
        # while not left and not right:
        #     if l < r:
        #         res.append(l)
        #         if len(left) > 0:
        #             l = left.pop(0)
        #         else:break
        #     else:
        #         res.append(r)
        #         if len(right) > 0:
        #             r = right.pop(0)
        #         else:break
        while left and right:
            #这里等于的情况，决定是稳定排序，在左边的先进入res中，后边的后进入
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))

        if left:
            res.extend(left)
        if right:
            res.extend(right)
        return res

    def shellSort(self,nums):
        #T(n) = nlogn,最好最坏均是
        #直接插入排序时，是稳定的，但是涉及到多个间隔时，就不一定了，
        #不严格规律：当不相邻元素之间交换元素时，一般都是不稳定的
        size = len(nums)
        d = size//2
        while d >0:
            for i in range(d,size):
                j = i-d
                while j >= 0 and nums[j] > nums[j+d]:
                    #这里需要交换，而不是直接插入排序中的直接后移
                    #后移会导致其他组合中的 数字乱
                    self.swap(nums,j,j+d)
            d //= 2

    def RadixSort(self,nums):
        #稳定，相同大小的元素，始终保持前后关系，
        #T(n) = k*n 非比较排序，即不是直接根据值的大小比较来排序的
        #先根据低位的大小，排好序；再根据高位排，
        #高位相同的值，根据之前的低位排序结果，已经排好序了
        size = len(nums)
        bit = 0
        maxx = max(nums)
        while maxx >0:
            bit += 1
            maxx //= 10
        mod = 10
        dev = 1
        while bit:
            bit -= 1
            dic = {}
            #各个bit位上的值分桶
            for i in range(size):
                bucket = nums[i]%mod//dev
                if bucket not in dic:
                    dic[bucket] = []
                dic[bucket].append(nums[i])
            cur = []
            #收集
            for i in range(10):
                if i in dic:
                    cur.extend(dic[i])
            nums = cur[:]
            mod *= 10
            dev *= 10
        return nums

    def insertSort(self,nums):
        #稳定，相等大小的值，直接在其后面插入即可，若放到前面，还有移位，
        #T(n) = n*2 最好：比较n次，不用移位，T(n) = n;最坏 T(n) = n*2
        #每次从未排序的数组中选取第一个数字n，在已排序的数组中，
        # 找到第一个下于n的值m，在其后面插入，期间，比n大的值均往后移
        size = len(nums)
        if size < 2:return
        for i in range(1,size):
            temp = nums[i]
            j = i-1
            while j >= 0 and nums[j] > temp:
                #后移动
                nums[j+1] = nums[j]
                j -= 1
            #插入
            nums[j+1] = temp

    def selectSort(self,nums):
        #不稳定，简洁版的冒泡排序法，当找到未排序序列中的最小值，然后与未排序起始位置的点交换，
        #所以，有可能 打乱相等值的前后顺序，
        #T(n) = n*2
        size = len(nums)


if __name__ == '__main__':
    so = Solution()
    nums = [3,44,38,5,4,3,15,38,37]
    print(nums)
    print(sorted(nums))
    # print(sorted(nums))
    # so.quickSort(nums, 0, len(nums) - 1)
    # print('quickSort:',nums)
    # nums = [3, 44, 38, 5, 4, 3, 15, 38, 37]
    # so.quickSort2(nums, 0, len(nums) - 1)
    # print('quickSort2:',nums)

    # so.bubbleSort2(nums)
    # print(nums)

    # so.heapSort(nums)
    # print(nums)

    # res = so.mergeSort(nums)
    # print(res)

    # so.insertSort(nums)
    # print(nums)

    # so.shellSort(nums)
    # print(nums)

    res = so.RadixSort(nums)
    print(res)

