# -*- coding:utf-8 -*-
'''
在一个字符串(0<=字符串长度<=10000，
全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

解法一：字典 T(n) = n+ n + nlogn
'''
#19:46 -- 20:00

class Solution:
    def FirstNotRepeatingChar(self, s):
        size = len(s)
        if size == 0:return -1
        dic = {}
        for i in range(size):
            temp = s[i]
            if temp not in dic:
                dic[temp] = [i]
            else:
                dic[temp].append(i)
        res= []
        for key,value in dic.items():
            if len(value) == 1:
                res.append(value[0])
        res.sort()
        if res:
            return res[0]
        else:
            return -1

if __name__ == '__main__':
    so = Solution()
    s = 'google'
    res = so.FirstNotRepeatingChar(s)
    print(res)


