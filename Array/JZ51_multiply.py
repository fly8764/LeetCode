# -*- coding:utf-8 -*-
'''
数列连乘，具有连续性；
如果每次都正常计算，则T(n)= o(n^2),从总共进行乘法的次数考虑。
B[i]都有两部分组成，A[i]左边的连乘left[i]，右边的连乘right[i]；
left[i] = A[0]*A[1]*...*A[i-1]
right[i] = A[i+1]*A[i+2]*...*A[n-1]
B[i] = left[i]*right[i]
由于：
left[i+1] = left[i]*A[i]
right[i] = right[i+1]*A[i+1]
所以可以把left[i],right[i]都分别求出来，就可以直接计算B[i]了，
这样T(n)= o(n)  O(n)=o(n)

还有一种节约空间的方法：
left[i]用B[i]代替，right[i]用tmp代替，对于right从右往左计算，
累乘到B[i]上。
这样空间复杂度减小到O(n)=o(l)，还少了一层循环。

'''
class Solution:
    # def multiply(self, A):
    #     n = len(A)
    #     if n < 2:
    #         return None
    #
    #     left = [1]*n
    #     right = [1]*n
    #     B = [1]*n
    #
    #     for i in range(0,n-1):
    #         left[i+1] = left[i]*A[i]
    #     for i in range(n-2,-1,-1):
    #         right[i]= right[i+1]*A[i+1]
    #     for i in range(n):
    #         B[i] = left[i]*right[i]
    #
    #     return B

    def multiply(self, A):
        n = len(A)
        if n < 2:return None

        B = [1]*n
        for i in range(0,n-1):
            B[i+1] = B[i]*A[i]
        tmp = 1
        for i in range(n-2,-1,-1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B





if __name__ == '__main__':
    func = Solution()
    A = [1,2,3,4,5]
    print(func.multiply(A))

