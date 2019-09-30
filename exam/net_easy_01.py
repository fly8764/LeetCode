class Solution:
    def find(self,x):
        if x < 10:
            return x
        bit = []
        while x >= 9:
            bit.append(9)
            x -= 9
        if x > 0:
            bit.append(x)

        # bit = list(map(str,bit))
        temp = []
        for i in range(len(bit)):
            temp.append(str(bit.pop()))
        # temp = bit[::-1]
        temp = ''.join(temp)
        return int(temp)

if __name__ == '__main__':
    t = int(input())
    so = Solution()

    while t:
        t -= 1
        x = int(input())
        print(so.find(x))






