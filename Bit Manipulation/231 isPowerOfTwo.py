class Solution:
    def isPowerOfTwo(self, n) :
        return n and not n &(n-1)
