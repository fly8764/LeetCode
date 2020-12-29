'''
单调递减队列
队列从队首到队尾单调递减
每次添加新的元素，都会和队尾元素比较大小，把小于新元素的值压缩掉
维持单调递减性；
另一方面，要保证队内索引和的范围在k内，即新元素i和队首元素之间的
长度在k内；
在往结果中存值时，要保证添加元素的下标和当前位置i的距离在k之内
'''
class Solution1:
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
            # 保证现在滑动窗口的长度在k内
            if i >= k - 1:
                res.append(nums[q[0]])
        return res


'''
2020/12/20 0:10
方法一 单调队列

方法二 优先队列（二叉堆）


'''

class Solution:
    # 暴力法，超时
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        res = []
        for i in range(n-k+1):
            res.append(max(nums[i:i+k]))
        return res

    def maxSlidingWindow2(self, nums, k):
        n = len(nums)
        res = []
        if n < 1:
            return res
        q = []
        for i in range(n):
            # 维持窗口宽度,当超出宽度时，从对首删除元素，而不是队尾。
            if q and i - q[0] + 1 > k:
                q.pop(0)
            # 把单调递减队列中的尾部元素和新值比较，小于新值的删除，最后把新值添加到队列末尾。
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            # 这里添加的是新元素的下标，不是新值，
            q.append(i)
            #保证当前的位置i能构成一个窗口
            if i >= k-1:
                res.append(nums[q[0]])
        return res









if __name__ == '__main__':
    so = Solution()
    print(so.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7],k = 3))