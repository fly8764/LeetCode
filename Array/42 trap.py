"""
方法一：双指针法
左指针max_left[i]:代表到目前位置i为止左边的最大高度，不包括位置i的高度
右指针max_right[i]：代表位置i右边的最大高度，也不包括位置i的高度
单方向遍历：
从左往右，因为每次位置i只用到了前面的一个位置的值，所以可以使用一个变量max_left来
实时标记；
但对于右指针max_right，需要从右往左遍历，所以，需要单独把遍历一次，求出；
左右两个方向遍历：
没整明白……
根据左右指针位置出的高度，选择左遍历还是右遍历，
"""
class Solution:
    def trap(self, height):
        size = len(height)
        max_left = 0
        res = 0
        max_right = [0]*size
        for i in range(size-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i+1])
        for i in range(1,size):
            max_left = max(max_left,height[i-1])
            minn = min(max_left,max_right[i])
            if minn > height[i]:
                res += minn - height[i]
        return  res

class Solution2:
    def trap(self, height):
        n = len(height)


if __name__ == '__main__':
    so = Solution()
    print(so.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

