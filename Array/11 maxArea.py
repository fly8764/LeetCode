class Solution:
    def maxArea(self, height):
        size = len(height)
        res = 0
        left,right = 0,size-1
        while left < right:
            if height[left] < height[right]:
                res = max(res,height[left]*(right - left))
                left += 1
            else:
                res = max(res,height[right]*(right-left))
                right -= 1
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.maxArea([1,8,6,2,5,4,8,3,7]))