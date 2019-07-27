class Solution:
    def find132pattern4(self, nums):
        stack = []
        third = float('-inf')

        for num in nums[::-1]:
            if num < third:
                return  True
            while(stack and num > stack[-1]):
                third = stack.pop()

            stack.append(num)
        return False

    def find132pattern(self, nums):
        size = len(nums)
        mn = 9999
        for j in range(size):
            mn = min(mn,nums[j])
            if mn == nums[j]:
                continue
            for k in range(size-1,j,-1):
                if mn < nums[k] and nums[j] >nums[k]:
                    return True
        return False



    def find132pattern3(self, nums):
        pass

        # n^3 超时
    def find132pattern0(self, nums):
        size = len(nums)

        for j in range(1, size - 1):
            for k in range(j + 1, size):
                if nums[k] < nums[j]:
                    for i in range(j):
                        if nums[i] < nums[k]:
                            return True

        return False


if __name__ == '__main__':
    so = Solution()
    res = so.find132pattern([1, 2, 3, 4]) # False
    print(res)

    res = so.find132pattern([3, 1, 4, 2])  # True
    print(res)

    res = so.find132pattern([-1, 3, 2, 0]) # True
    print(res)
