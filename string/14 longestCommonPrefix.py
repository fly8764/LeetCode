'''
注意这里要求的是前缀，必须是前缀，前缀一旦遇到不相等的值，就要中断。
'''
class Solution:
    def longestCommonPrefix(self, strs):
        size = len(strs)
        if size < 1:
            return ''
        minSize = min(len(s) for s in strs)
        res = ""
        for i in range(minSize):
            temp = strs[0][i]
            flag = True
            for s in strs:
                if s[i] != temp:
                    flag = False
                    break
            if flag:
                res += temp
            else:
                break
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.longestCommonPrefix(["flower","flow","flight"]))
    print(so.longestCommonPrefix(["dog","racecar","car"]))
    print(so.longestCommonPrefix(["aca","cba"]))