'''
动态规划
根据以前的状态，来决定当前的状态
dp[i]:代表s[:i]（不包括s[i],到s[i-1]）是否符合要求
对于s[:i+1],观察dp[j] and s[j:i+1]，如果以前的dp[j]能够满足要求，并且后面的也是
则符合要求
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        size = len(s)
        dp = [0]*(size +1)
        dp[0] = 1
        length = [len(x) for x in  wordDict]
        length = set(length)
        for i in range(size):
            for item in length:
                if dp[i-item+1] and s[i-item+1:i+1] in wordDict:
                    dp[i+1] = 1
                    break
            #这里也可以 遍历字典中存在的长度，而不必所有的长度都尝试一次
            # for j in range(i,-1,-1):
            #     if dp[j] and s[j:i+1] in wordDict:
            #         dp[i+1] = 1
            #         #找到即可停止循环了
            #         break
        return dp[-1] == 1


if __name__ == "__main__":
    so = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(so.wordBreak(s,wordDict))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(so.wordBreak(s, wordDict))

