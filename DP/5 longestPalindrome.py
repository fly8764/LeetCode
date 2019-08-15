class Solution:
    def longestPalindrome(self, s):
        pass


# class solution():
#     def __init__(self):
#         pass
#
#     def generator(self,s):
#         length = len(s)
#         if length == 0:
#             return ''
#
#         new_s = '#'
#         for i in range(length):
#             new_s += s[i]
#             new_s += '#'
#         return new_s
#
#     def longestPalindrome(self,s):
#         if len(s) ==0:
#             return ""
#
#         new_s = self.generator(s)
#         length = len(new_s)
#         mx = 0
#         id = 0
#         max_num = 1
#         longest_str = new_s[0:1]
#         p = [0 for _ in range(length)]
#         for i in range(length):
#             if i < mx:
#                 p[i] = min(p[2*id - i],mx-i)
#             elif i == mx:
#                 p[i] = 1
#
#             while(i-p[i] >= 0 and i+p[i]<length and new_s[i+p[i]]==new_s[i-p[i]]):
#                 p[i] += 1
#
#             if i+p[i] > mx:
#             # if i+p[i] > mx and i+ p[i] < length:
#                 mx = i + p[i]
#                 id = i
#
#             if p[i]-1 >= max_num:#这里需要加上 = 不然在 只有一个字符时，不会进入更新；或者不加 = 但是要把 max_num 初始化为0而不是1(快一点)
#                 max_num = p[i]-1
#                 longest_str = new_s[i-p[i]+1:i+p[i]].replace('#','')
#         return longest_str

# if __name__ == '__main__':
    # so = solution()
    # res = so.longestPalindrome('a')
    # print(res)


