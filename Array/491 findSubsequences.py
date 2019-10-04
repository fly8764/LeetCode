class Solution:
    def findSubsequences(self, nums):
        #这种暴力的方法 超时
        size = len(nums)
        if size < 2:return []
        seq = [ [ [nums[i]] ]  for i in range(size)]
        res = []
        for i in range(1,size):
            #以第i个值为结尾的子序列 遍历结束后，要更新seq[i]
            cur = []
            for j in range(i):
                if nums[i] >= nums[j]:
                    for item in seq[j]:
                        new = item+[nums[i]]
                        if new not in seq[i]:
                            #可以在这里直接往seq[i]中添加新元素
                            seq[i].append(new)
                            # cur.append(new)
                        cur.append(new)
                        if new not in  res and len(new)>1:
                            res.append(new)
            # seq[i].extend(cur)
        return res


if __name__ =='__main__':
    so = Solution()
    nums= [4, 6, 7, 7]
    print(so.findSubsequences(nums))




