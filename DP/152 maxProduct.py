class Solution:
    def maxProduct(self, nums):
        size = len(nums)
        res = max_sub = min_sub = nums[0]

        for i in range(1,size):
            if nums[i]<0:
                max_sub, min_sub = min_sub,max_sub
            max_sub = max(max_sub*nums[i],nums[i])
            min_sub = min(min_sub*nums[i],nums[i])

            res = max(res,max_sub)

        # for i in range(1,size):
        #     if nums[i]!= 0:
        #         temp *= nums[i]
        #         max_sub = max(max_sub, temp,nums[i])
        #     else:
        #         temp = 1
        #         zero = 0
        #         max_sub = max(max_sub, zero)
            # max_sub = max(max_sub,temp,zero)
        # for i in range(1,size):
        #     temp = max(temp*nums[i],nums[i])
        #     max_sub = max(max_sub,temp)


        # for i in range(1,size):
        #     if temp != 0:
        #         temp *= nums[i]
        #     else:
        #         temp = nums[i]
        #     max_sub = max(max_sub,temp)

        return max_sub

if __name__ == '__main__':
    so = Solution()
    res = so.maxProduct([3,-1,4]) #4 #
    print(res)
    res = so.maxProduct([-2,0,-1]) #0 [-2,0,-1] [2,3,-2,4] [3,-1,4] [-4,-3] [-2,3,-4]
    print(res)
    res = so.maxProduct([2,3,-2,4]) #6
    print(res)
    res = so.maxProduct( [-4,-3]) # 12
    print(res)
    res = so.maxProduct( [-2,3,-4]) #24
    print(res)
    res = so.maxProduct([2,-5,-2,-4,3]) #24
    print(res)

