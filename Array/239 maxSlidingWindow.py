'''
单调递减队列
队列从队首到队尾单调递减
每次添加新的元素，都会和队尾元素比较大小，把小于新元素的值压缩掉
维持单调递减性；
另一方面，要保证队内索引和的范围在k内，即新元素i和队首元素之间的
长度在k内；
在往结果中存值时，要保证添加元素的下标和当前位置i的距离在k之内
'''
class Solution:
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        size = len(nums)
        if size < 1:return []
        res = []
        # q = deque()
        q = []
        for i in range(size):
            if q and i - q[0]+ 1> k:
                # q.popleft()
                q.pop(0)
            #维持一个单调递减队列
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i -k + 1 >= 0:
                res.append(nums[q[0]])
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7],k = 3))