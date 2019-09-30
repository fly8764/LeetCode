# class Solution:
#     def getNext(self,s):
#         size = len(s)
#         next = [0]*(size)
#         next[0]= -1
#         k = -1
#         j = 0
#         while j < size-1:
#             if k == -1 or s[j] == s[k]:
#                 j += 1
#                 k += 1
#                 next[j] = k
#             else:
#                 k = next[k]
#         return next
#
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle == '':
#             return 0
#         size1 = len(haystack)
#         size2 = len(needle)
#         if size1 < size2:
#             return -1
#         next = self.getNext(needle)
#         i,j = 0,0
#         while i < size1 and j < size2:
#             if j == -1 or haystack[i] == needle[j]:
#                 i += 1
#                 j += 1
#             else:
#                 j = next[j]
#         if j == size2:
#             return i - j
#         else:
#             return -1

class Solution:
    def getNext(self,s):
        size = len(s)
        next = [0]*size
        next[0] = -1
        k = -1
        j = 0
        while j < size -1:
            #if 中的第一个条件别写错了，k==-1而不是j == -1
            #s[k]:前缀 s[j]:后缀
            if k == -1 or s[j] == s[k]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next

    def strStr(self,haystack,needle):
        size1 = len(haystack)
        size2 = len(needle)
        if size2 > size1:
            return -1
        next = self.getNext(needle)
        print(next)
        i,j = 0,0
        while i < size1 and j < size2:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == size2:
            return i - j
        else:
            return -1

class Solution2:
    def getNext(self,s):
        size = len(s)
        next = [0] * size
        #当目标串的首字符和目标串中的字符不相等时
        #两者都后移一位
        next[0] = -1
        j = 0
        k = -1
        while j < size-1:
            #这里j最大到size-2,因为后面赋值时前，j += 1
            #s[k]:前缀  s[j]:后缀
            if k == -1 or s[j] ==s[k]:
                j += 1
                k += 1
                next[j] = k
            else:
                #利用已得出的next信息
                j = next[j]
        return next

    def strStr(self,s,t):
        size1 = len(s)
        size2 = len(t)
        if size2 == 0:return 0
        if size2 > size1:return -1
        next = self.getNext(t)
        print(next)
        i,j = 0,0 #i:模式串的下标 j:目标串的下标
        while i < size1 and j < size2:
            if j == -1 or s[i] == t[j]: #这里是or别忘了
                i += 1
                j += 1
            else:
                j = next[j]
        if j == size2:
            return i-j
        else:
            return -1

class Solution3:
    def getNext(self,t):
        size = len(t)
        next = [0]*size
        next[0] = -1
        #j代表循环的位置，
        # k代表next[j]对应的值，t[:j]的最长公共前缀长度
        j = 0
        k = -1
        while j < size-1:
            #这里j最大到size-2，因为后面有j+=1，会使得j到达size-1
            if k == -1 or t[j] == t[k]:
                j += 1
                k += 1
                next[j] = k
            else:
                k = next[k]
        return next


    def strStr(self,s,t):
        next = self.getNext(t)
        size1 = len(s)
        size2 = len(t)

        if size2 > size1:return -1
        i,j = 0,0
        while i < size1 and j < size2:
            if j == -1 or s[i] == t[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == size2:
            return i - size2
        else:
            return -1



if __name__ == '__main__':
    so = Solution3()
    print(so.strStr("hello", "ll"))
    print(so.strStr("aaaaa", "bba"))





