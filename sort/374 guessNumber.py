# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    #返回的是目标值相对于 猜测值，1：目标 大于猜测，-1：目标小于猜测
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:return
        left,right = 0,n
        while left < right:
            mid = (left + right) >> 1
            if guess(mid) <= 0:
                #这里要加上等于号，比目标值大或等于，都有可能
                right = mid
            else:
                #比目标值小的一定不是要求的值，反之，比目标值大或等于，都有可能
                left = mid + 1
        return left

