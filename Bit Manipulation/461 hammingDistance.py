class Solution:
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')

    def hammingDistance0(self, x, y):
        res = x ^ y
        cnt = 0

        while res:
            res &= (res-1)
            cnt += 1
        return  cnt



if __name__ == "__main__":
    so = Solution()
    res = so.hammingDistance(1,4)
    print(res)