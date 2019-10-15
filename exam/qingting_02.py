class Solution:
    def quickSort(self, nums, s, t):
        temp = nums[s]
        i, j = s, t
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

if '__main__' ==  '__main__':
    so = Solution()
    nums = []
    path = ''
    text = open(path,'r')
    res = []
    for line in text.readlines():
        temp = map(int(),line.split())
        nums.extend(temp)
    so.quickSort(nums,0,len(nums)-1)
    for num in nums:
        print(num)
