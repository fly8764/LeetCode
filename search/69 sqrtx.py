class Solution:
    def mySqrt(self, x):
        #使用右中位数，
        #若使用左中位数，会陷入死循环
        left,right = 0,x
        # mid = (left + right)>>1

        while left < right:
            mid = (left + right+1) >> 1
            if mid**2 > x:
                right = mid -1
            else:
                left = mid
        return left


if __name__ == '__main__':
    so = Solution()
    #8
    print(so.mySqrt(4))


