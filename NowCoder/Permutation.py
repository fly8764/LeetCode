# -*- coding:utf-8 -*-
'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串
abc,acb,bac,bca,cab和cba。

输入描述：
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

要考虑 重复字符的情况，其结果会有重复，所以要在最后排除掉重复值。
'''
#20:00 -- 20:25
class Solution:
    def __init__(self):
        self.res = []

    def dfs(self,s,cur):
        size = len(s)
        if size == 0:
            self.res.append(cur)
        else:
            for i in range(size):
                # temp = s[:]
                self.dfs(s[:i]+s[i+1:],cur + s[i])

    def Permutation(self, ss):
        size = len(ss)
        if size == 0:return []
        nums = sorted(ss)
        self.dfs(nums,'')
        res = []
        for item in self.res:
            if item not in res:
                res.append(item)
        return res

if __name__ == '__main__':
    so = Solution()
    ss = 'a'
    res = so.Permutation(ss)
    print(res)
