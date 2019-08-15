class Solution:
#   动态规划法
#     def longestPalindrome(self, s):
#         length = len(s)

#         if length ==0:
#             return ''
#         longest = 1
#         result = s[0]

#         dp = [[0 for _ in range(length)] for __ in range(length) ]

#         for r in range(1,length):
#             for l in range(r):
#                 if s[l]==s[r] and (r-l<=2 or dp[l+1][r-1]):
#                     dp[l][r] = 1
#                     cur_len = r-l+1
#                     if cur_len > longest:
#                         longest = cur_len
#                         result = s[l:r+1]
#         return result

    def longestPalindrome(self, s):
        if not s:
            return ''

        size = len(s)
        res = s[0] #这里不能直接初始化一个空字符串
        dp = [[0]*size for _ in range(size)]
        max_len = float('-inf')

        for r in range(1,size):
            for l in range(r):
                if s[l] == s[r] and (r-l <=2 or dp[l+1][r-1]): #这里and 后面要用括号括起来，不然会报错
                    dp[l][r] = 1
                    if max_len < r-l +1:
                        max_len = r-l+1
                        res = s[l:r+1]
        return res

                # if dp[l][r] and



if __name__ == '__main__':
    so = Solution()
    res = so.longestPalindrome("cbbd")
    print(res)
    # def check(self,s,left,right):
    #     length = 0
    #     max_str = ''
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         length = right - left + 1
    #         max_str = s[left:right + 1]
    #         left -= 1
    #         right += 1
    #
    #     return length,max_str
    #
    # def longestPalindrome(self, s):
    #     #中心扩散法
    #     if not s:
    #         return ''
    #     max_num = 0
    #     max_str = s[0]
    #     cur_sub = ''
    #
    #     for i in range(len(s)):
    #         left_num,left_str = self.check(s,i,i)
    #         right_num,right_str = self.check(s,i,i+1)
    #
    #         if left_num > right_num:
    #             cur_sub = left_str
    #         else:
    #             cur_sub = right_str
    #         if len(cur_sub) > max_num:
    #             max_str = cur_sub
    #             max_num = len(cur_sub)
    #
    #     return max_str

    # def generate(self,s):
    #     new = '#'
    #     for i in s:
    #         new +=i + '#'
    #     return new
    #
    # def longestPalindromeSubseq(self,s):
    #     if not s:
    #         return ''
    #     longest = 1
    #     maxSub = s[0]
    #
    #     l = self.generate(s)
    #     size = len(l)
    #     dp = [0]*size
    #     id = 0
    #     mx = 0
    #
    #     for i in range(len(l)):
    #         if i < mx:
    #             dp[i] = min(dp[2*id-i],mx-i)
    #         else:
    #             dp[i] = 1
    #         while i - dp[i] >= 0 and i + dp[i] < size and l[i-dp[i]] == l[i+dp[i]]:
    #             dp[i] += 1
    #
    #         if i+ dp[i] > mx:
    #             mx = i + dp[i]
    #             id = i
    #         if dp[i]- 1 > longest:
    #             longest = dp[i]- 1
    #             maxSub = l[i-dp[i]+1:i+dp[i]].replace('#',"")
    #     return maxSub

    # class Solution():
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


