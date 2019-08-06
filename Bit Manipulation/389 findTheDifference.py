class Solution:
    def findTheDifference(self, s, t):
        #异或 ord(str) 返回字符(串)的ascii码
        ans = ord(t[-1])
        for i in range(len(s)):
            ans ^= ord(s[i])
            ans ^= ord(t[i])
        return chr(ans)

    def findTheDifference0(self, s, t):
        #哈希表(字典）
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1

            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1

        if t[-1] in t_dict:
            t_dict[t[-1]] += 1
        else:
            t_dict[t[-1]]  = 1

        for key,value in t_dict.items():
            if key not in s_dict or t_dict[key] != s_dict[key]:
                return key

if __name__ == '__main__':
    so = Solution()
    s = "abcd"
    t = "abcde"
    res = so.findTheDifference(s,t)
    print(res)

