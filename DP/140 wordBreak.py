class Solution():
    # def dfs(self,s,cur):
    #     if s == '':
    #         self.res.append(cur)
    #         return
    #     for i in range(len(s)):
    #         if s[:i+1] in self.wordDict:
    #             self.dfs(s[i+1:],cur + [s[:i+1]])
    #
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: List[str]
    #     """
    #     #暴力 递归法,对所有的长度都遍历一次，长度1：n，
    #     #其实只要遍历字典中有的长度即可，从而可以减小遍历的数量，非暴力
    #     self.res = []
    #     self.wordDict = wordDict
    #     cur = []
    #     self.dfs(s,cur)
    #     ret = []
    #     for i in range(len(self.res)):
    #         ret.append(' '.join(self.res[i]))
    #     return ret
    def check(self,s,wordDict):
        size = len(s)
        dp= [0]*(size+1)
        #这个dp[0]等于1别忘了，不然后面都会出错
        dp[0] = 1 #空字符串 一定存在
        length = set(self.length)
        for i in range(size):
            for item in length:
                if len(s) >= item and dp[i-item+1] and s[i-item+1:i+1] in wordDict:
                    dp[i+1] = 1
        return dp[-1] == 1

    def dfs(self,s,cur):
        if self.check(s,self.wordDict):
            if s == '':
                self.res.append(' '.join(cur))
                # res.append(' '.join(cur))
            else:
                for item in self.length:
                    if len(s) >= item and s[:item] in self.wordDict:
                        self.dfs(s[item:], cur + [s[:item]])

    def wordBreak(self, s, wordDict):
        self.wordDict = wordDict
        self.length = [len(x) for x in wordDict]
        #这一步 集合，去重别忘了，不然会重复计算很多次
        self.length = set(self.length)
        self.res = []
        # res = []
        self.dfs(s,[])
        return self.res
        # return res

class Solution2():
    def wordBreak(self,s,wordDict):
        result = []
        stride = [len(word) for word in wordDict]
        stride_set = set(stride)
        self.dfs(s,wordDict,stride_set,[],result)
        return result

    def dfs(self,s,wordDict,stride_set,curr_res,result):
        if self.check(s,wordDict):
            if len(s)==0:
                result.append(' '.join(curr_res))
            else:
                for stride in stride_set:
                    if stride<= len(s) and s[:stride] in wordDict:
                        self.dfs(s[stride:],wordDict,stride_set,curr_res+[s[:stride]],result)

    def check(self,s,wordDict):
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for i in range(len(s)):
            for j in range(i,-1,-1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(so.wordBreak(s,wordDict))
    s = 'a'
    wordDict = ['a']
    print(so.wordBreak(s, wordDict))
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(so.wordBreak(s, wordDict))




