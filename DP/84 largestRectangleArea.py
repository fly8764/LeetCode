class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                res = max(res,heights[stack.pop()]*(i-1-stack[-1]))
            stack.append(i)
        return res

    def largestRectangleArea0(self, heights):
        #维护一个递增栈，在while循环中，每次取出栈顶对应的高度，往右直到i(因为升栈，所以右边的都比当前的高)，作为宽度
        #即从i开始，逐渐往左扩展，减小高度，增加宽度，计算新的矩形面积，前提是一个递增栈
        stack = [-1]
        max_area = 0
        size = len(heights)

        for i in range(size):
            #这里在维护一个递增栈：heights[stack[-1]] >= heights[i]，
            #不满足，即小于 heights[i]的，直接压入栈中
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area,heights[stack.pop()]*(i-1-stack[-1]))
            stack.append(i)

        while stack[-1] != -1:
            max_area = max(max_area,heights[stack.pop()]*(size-1 - stack[-1]))

        return max_area




