class Solution:
    def find(self,s):
        size = len(s)
        res = []
        for i in range(1,size+1):
            temp = s[:i]
            l = len(temp)
            if size%l == 0:
                n = int(size/l)
                if temp*n == s:
                    return l
                    # res.append(l)
        # print(res)
        return -1

    def res(self,s):
        ind = self.find(s)
        temp = ''
        for i in range(ind-1):
            temp +='0'
        temp += '1'
        res = temp*int(len(s)/ind)
        # size = len(s)
        # res = [0]*size
        # res[-1] = 1
        # for item in ind:
        #     cnt = 1
        #     index = item
        #     while index < size:
        #         res[index-1] = 1
        #         cnt +=1
        #         index = item*cnt
        # ret = list(map(str,res))
        # ret = ''.join(ret)

        return res




        # for i in range(ind-1):
        #     temp += '0'
        # temp += '1'
        # res = temp*int((len(s)/ind))
        # return res


if __name__ =='__main__':
    s = input()
    so = Solution()
    res = so.res(s)
    # res = so.res(s)
    print(res)





