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
'''
双指针+贪心
左右指针分别指向首尾，比较两个指针的高度，选择矮的作为高度，然后矮个往中间移动；遍历一遍，
直至结束。
这种解法相比于暴力枚举法，感觉遗漏了很多中情况，下面解释没计算的，其实都考虑进去了。
1.只把矮个的指针往中间移动，不移动高个的指针呢？
一方面另一个指针在往中间移动，长度在减小；另一方面，移动高个的指针，新的高度只会小于
或等于矮个，面积一定会减小，所以只移动矮个的指针，不移动高个的指针。
2.每次移动矮个指针至新的位置，但是移动之前，左边矮个到右边高个指针的其它情况还没有考虑，
不会遗漏吗?
在状态 S(i, j)下向内移动短板至 S(i + 1, j)（假设 h[i] < h[j]h[i]<h[j] ），
则相当于消去了 {S(i, j - 1), S(i, j - 2), ... , S(i, i + 1)}状态集合。
而所有消去状态的面积一定 <= S(i, j)：
宽度：一定减小
高度：短板理论，高度一定小于等于h[i]
所以消去的状态一定小于S(i,j)。

https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/

'''
class Solution2:
    def maxArea(self, height):
        n = len(height)
        left,right = 0,n-1

        res = 0
        while left < right:
            if height[left] < height[right]:
                res = max(res,height[left]*(right-left))
                left += 1
            else:
                res = max(res,height[right]*(right-left))
                right -= 1
        return res



if __name__ == '__main__':
    so = Solution2()
    print(so.maxArea([1,8,6,2,5,4,8,3,7]))