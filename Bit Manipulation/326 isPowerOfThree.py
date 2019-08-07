class Solution:
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        temp = 1
        while temp < n:
            #这里要加括号，否则，左移后的结果会及时更新temp，加号后面的直接使用更新后的
            #temp = temp<<1 + temp
            #temp = (temp<<1) + temp
            temp *= 3
        if temp == n:
            return True
        else:
            return False

if __name__ == "__main__":
    so = Solution()
    res = so.isPowerOfThree(27)
    print(res)

