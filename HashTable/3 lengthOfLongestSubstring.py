'''
双指针 滑动窗口
用一个字典保存字符的出现位置，方便后面查询字符是否重复出现，
当重复字符出现时，要更新字符的新位置，
类似于滑动窗口，没有重复字符时，不断加长窗口；当遇到重复字符时，窗口缩小为当前字符大小
即一个字符。
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        size = len(s)
        if size < 1:
            return 0
        #dic中保存字符s[i]出现的位置
        dic = {}
        left = 0 #子串左边起始点
        res = 1
        for i in range(size):
            #当重读字符出现时，判断上一次出现的位置，并和当前的左边界比较，
            #去靠右的位置；为了防止一些字符在当前左边界的左边出现，这种字符的左边界
            #不需要，所以要使用max()来取左边界
            if s[i]in dic:
                left = max(left,dic.get(s[i]) + 1)

            dic[s[i]] = i
            res = max(res,i-left + 1)
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLongestSubstring("abcabcbb"))
    print(so.lengthOfLongestSubstring("bbbbb"))
    print(so.lengthOfLongestSubstring("pwwkew"))
    print(so.lengthOfLongestSubstring("abba"))



