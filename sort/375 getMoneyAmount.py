def guess(num):
    if num > target:
        return -1
    elif num < target:
        return 1
    else:return 0

#这一题不是二分法，是动态规划
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:return 0
        left,right = 1,n
        money = 0
        while left < right:
            mid = (left + right)>>1
            temp = guess(mid)
            if temp > 0:
                left = mid + 1
                money += mid
            elif temp < 0:
                right = mid
                money += mid
            else:
                return money
        return money


if __name__ == '__main__':
    target = 8
    so = Solution()
    res = so.getMoneyAmount(10)
    print(res)
