# -*- coding:utf-8 -*-
'''
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,
他马上就写出了正确答案是100。但是他并不满足于此,
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述：
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，
序列间按照开始数字从小到大的顺序

思路：
这里用到的也是双指针，不过这个不是从列表的两端往中间移动；
连续数列之和，当变短时，和减小；变长时，和增大；但是，序列整体上是向右移动的，
和小时，右边界 右移，增长序列；和小时，左边界右移，缩短序列；整体都是右移；

'''
#21:21 -- 23:14
class Solution:
    def __init__(self):
        self.res = []

    def save(self,small,big):
        cur = []
        for i in range(small,big+1):
            cur.append(i)
        self.res.append(cur)


    def FindContinuousSequence(self, target):
        small = 1
        big = 2
        mid = (1+target)//2
        cur = small + big

        while small < mid:
            if cur == target:
                self.save(small,big)
            while cur > target and small < mid:
                #注意这里在变化的是左边界，一直在递增，所以判断条件里面要写 small
                cur -= small
                small += 1
                if cur == target:
                    self.save(small,big)

            big += 1
            cur += big

        return self.res

if __name__ == '__main__':
    so = Solution()
    res = so.FindContinuousSequence(4)
    print(res)


