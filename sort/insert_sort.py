class Solution:
    def __init__(self):
        self.size = 0

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
    #这里理解错了，
    #实际上，每次swap 都是在调整 pivot的位置，当左右指针相等时，pivot的位置也调整好了，
    #不用在最后再次调整 开头与i的位置元素，即 nums[left] = temp
    #     left = s
    #     right = t
    #     if s < t:
    #         temp = nums[s]
    #         while left < right: #从两边往中间扫描，直到left == right
    #             while right > left and nums[right] > temp:
    #                 right -= 1
    #             if left < right: #看是上面哪个条件跳出来的
    #             先不管 nums[left]的大小如何，先交换到右边的nums[right]再说，到那边再比较
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
    #         nums[left] = temp #这一步不需要
    #         self.quickSort(nums,s,left-1)
    #         self.quickSort(nums,left+1,t)

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def partition(self,nums,s,t):
        #从左往右逐个扫描，而不是像上面那个解法，左右两边同时向中间扫描，直到相等
        #这种方法 每次需要调整位置时，都要交换一次位置，操作数比较多
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
            # 不要把partition写在里面，不然变量的作用范围容易受到影响；
            # 最好写在外面
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

    def buildMaxheap(self,nums):
        #这里从size//2开始往前遍历有两个好处
        #1.类似于从完全二叉树的倒数第二层开始调整堆，2*i+1 2*i+2分别对应 节点i的左右子节点
        #2.从后往前，从下往上，一层一层地“筛选”，保证最大的元素在堆顶。类似于冒泡
        self.size = len(nums)
        for i in range(self.size//2,-1,-1):
            self.heapify(nums,i)

    def heapify(self,nums,i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i

        if left < self.size and nums[left] > nums[largest]: largest = left
        if right < self.size and  nums[right] > nums[largest]: largest = right
        if largest != i:
            #继续递归，使得上面调整后，下面的堆 仍然符合最大/小 堆的要求
            self.swap(nums, i, largest)
            self.heapify(nums, largest)

    def heapSort(self,nums):
        #最大堆排序
        self.bubbleSort(nums)
        for i in range(self.size-1,0,-1):
            #把堆顶元素放到后面，最小元素放在堆顶，后面再重新调整堆；同时为处理的列表长度减1
            self.swap(nums,0,i)
            self.size -= 1
            #从堆顶开始重新调整堆，原先的堆整体往上升了一层
            self.heapify(nums,0)
        return nums

    def buildMinheap(self,nums):
        self.size = len(nums)
        for i in range(self.size//2,-1,-1):
            self.heapifyMin(nums,i)

    def heapifyMin(self,nums,i):
        left = 2*i + 1
        right = 2*i + 2
        least = i
        if left < self.size and nums[left] < nums[least]: least = left
        if right < self.size and nums[right] < nums[least]:least = right
        if least != i:
            self.swap(nums,i,least)
            self.heapifyMin(nums,least)

    def heapSortMin(self,nums):
        #T(n) = (n/2)logn + nlogn
        #要保证 不改变 完全二叉树的 结构，因为在调整堆时，有 left = 2*i + 1 等的存在，要用到堆的结构
        #因此，最小堆排序只能 额外申请一个数组，每次保存 堆顶的最小值，
        #之后把右小角的值 交换到 堆顶，删除末尾元素，修改堆的长度，再次调整堆
        res = []
        self.buildMinheap(nums)
        for i in range(self.size):
            res.append(nums[0])
            #把最大元素放到堆顶，之后删掉最后一个元素，修改堆的长度
            self.swap(nums,0,self.size-1)
            nums.pop()
            self.size -= 1
            self.heapifyMin(nums,0)
        return res

    def radixSort(self,nums):
        maxx = max(nums)
        bit = 0
        while maxx:
            bit += 1
            maxx //= 10
        mod = 10
        dev = 1
        for i in range(bit):
            temp = {}
            for j in range(len(nums)):
                bucket = nums[j]%mod//dev
                if bucket not in temp:
                    temp[bucket] = []
                temp[bucket].append(nums[j])
            cur = []
            for idx in range(10):
                if idx in temp:
                    cur.extend(temp[idx])
            nums = cur[:]
            mod *= 10
            dev *= 10
        return nums


if __name__ == '__main__':
    so = Solution()
    nums = [4,1,5,3,8,10,28,2]
    print(nums,'raw')
    print(sorted(nums),'gt')
    # res = so.insetSort(nums[:])
    # print(res)
    # res2 = so.shellSort(nums[:])
    # print(res2)
    # res3 = so.bubbleSort(nums[:])
    # print(res3,'bubbleSort')
    # so.quickSort(nums,0,len(nums)-1)
    # print(nums)
    # res = so.mergeSort(nums)
    # print(res)
    # res = so.heapSort(nums[:])
    # print(res)
    # res = so.heapSortMin(nums[:])
    # print(res)
    res = so.radixSort(nums[:])
    print(res)