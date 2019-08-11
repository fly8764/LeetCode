import sys


# def find(n, s, e, target, cur,res):
#     if n < 0 or target < 0:
#         return
#
#     if target == 0 and n == 0:
#         res.append(cur)
#
#     for i in range(s, e):
#         if n-1 >-1 and target -i > -1:
#             find(n - 1, i + 1, e, target - i, cur + [i],res)
#         else:break
#
#     return res


class Solution:
    def __init__(self):
        self.res = []

    def find(self,n, s, e, target, cur):
        if n < 0 or target < 0:
            return

        if target == 0 and n == 0:
            # self.res += 1
            self.res.append(cur)


        for i in range(s, e):
            if n-1 >-1 and target -i > -1:
                self.find(n - 1, i + 1, e, target - i, cur + [i])
            else:break

        # for i in range(s, e):
        #     self.find(n - 1, i + 1, e, target - i, cur + [i])


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    values = list(map(int,line.split()))
    n,s = values[0],values[1]

    so = Solution()
    so.find(n,1,s,s,[])
    res = so.res
    print(res)
    print(len(res))

    # res = find(n, 1, s, s, [],[])
    # print(res)

    # print(len(res))
