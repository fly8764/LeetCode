class Solution:
    def find(self,nums):
        size = len(nums)
        if size < 2:return size

        tail = [nums[0]]
        for i in range(1,size):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            left,right = 0,len(tail) -1
            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)


if __name__ == '__main__':
    so = Solution()
    nums = list(map(int,input().split(',')))
    res = so.find(nums)
    print(res)