class Solution:
    def find(self,minn,maxx,qu,cnt):
        pass


    # def add(self,nums,n,qu,cnt):
    #     single = []
    #     for i in nums:
    #         if i not in single:
    #             single.append(i)
    #
    #     minn = min(single)
    #     maxx = max(single)
    #     res ={}
    #
    #     # for item in qu:
    #     #     if item[0] <= maxx or item[1] >= minn:
    #     #         left = max(minn,item[0])
    #     #         right = min(maxx,item[1])
    #     #         for i in range(left,right+1):
    #     #             if i not in res:
    #     #                 res[i] = 1
    #     #             else:
    #     #                 res[i] += 1
    #     # ret = []
    #
    #     if item[0] <= maxx or item[1] >= minn:
    #         left = max(minn, item[0])
    #         right = min(maxx, item[1])
    #         for i in range(left, right + 1):
    #             if i not in res:
    #                 res[i] = 1
    #             else:
    #                 res[i] += 1
    #
    #     for i in range(n):
    #         if nums[i] in res:
    #             cnt.append(res[nums[i]])
    #         else:
    #             cnt.append(0)
    #
    #     return cnt


if __name__ == '__main__':
    so = Solution()
    t = int(input())
    idx = 1
    while t:
        t -= 1
        line = list(map(int,input().split()))
        n,m = line[0],line[1]
        nums = list(map(int,input().split()))
        dic = {}
        for i in nums:
            dic[i] = 0

        minn = min(nums)
        maxx = max(nums)

        while m:
            m -= 1
            qu = list(map(int,input().split()))
            if qu[0] <= maxx or qu[1] >= minn:
                left = max(qu[0], minn)
                right = min(qu[1], maxx)
                for i in range(left, right + 1):
                    dic[i] += 1

        print('Case #%d:' % idx)
        idx += 1
        for i in range(n):
            print(dic[nums[i]])

        # qu = []
        # while m:
        #     m -= 1
        #     qu.append(list(map(int,input().split())))
        # res = so.add(nums,n,qu)
        # print('Case #%d:'%i)
        # i += 1
        # for item in res:
        #     print(item)