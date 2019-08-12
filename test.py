class Solution:
    def find(self,n):
        n += 5

    def test(self,n):
        self.find(n)
        print(n)
        return n


if __name__ == "__main__":
    so = Solution()
    test = so.test(0)
    print(test)
    # if test:
    #     print(9)
    # else:
    #     print(0)