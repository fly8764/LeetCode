class Solution:
    def test(self,n):
        if n:
            return n



if __name__ == "__main__":
    so = Solution()
    test = so.test(0)
    print(test)
    if test:
        print(9)
    else:
        print(0)