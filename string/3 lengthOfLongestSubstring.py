class Solution:
    def lengthOfLongestSubstring(self, s):
        size = len(s)
        if size < 1:
            return 0
        res = 0
        dic = {}
        start = 0
        for end in range(size):
            temp = s[end]
            if temp in dic:
                #这里要取start的较大值，而不是单单的dic.get(temp)
                #因为有些重复字符第一次出现的位置靠左，dic.get(temp)偏小
                #实际当前的start已经靠后了，所以，要使用max，取最大值
                #eg：abba
                start = max(dic.get(temp),start)
                # start = dic.get(temp)
            res = max(res,end-start+1)
            dic[temp] = end + 1
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLongestSubstring("abcabcbb"))
    print(so.lengthOfLongestSubstring("bbbbb"))
    print(so.lengthOfLongestSubstring("pwwkew"))