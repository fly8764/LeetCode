'''
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

链接：https://leetcode-cn.com/problems/edit-distance

思路：动态规划求解 从低倒上
dp[i][j]:表示 s1[:i+1] s2[:j+1] 的转换距离，
当s1[i] == s2[j]时，dp[i][j] = dp[i-1][j-1] 即跳过，不进行操作
当s1[i] != s2[j]时，dp[i][j] = min(dp[i-1][j]+1, #s1删除操作s1[i],参考dp[i-1][j],操作数加一
                                   dp[i][j-1]+1, #s1插入s2[j]，参考dp[i][j-1]
                                   dp[i-1][j-1]+1) #s1把s1[i]为s2[j]，参考dp[i-1][j-1]

'''

class Solution:
    def minDistance(self, word1, word2):
        size1 = len(word1)
        size2 = len(word2)
        dp = [[0]*(size2+1) for _ in range(size1+1)]

        for i in range(size1+1):
            dp[i][0] = i
        for j in range(size2+1):
            dp[0][j] = j

        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,
                                   dp[i][j-1]+1,
                                   dp[i-1][j-1]+1)
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'ros'
    so = Solution()
    res = so.minDistance(word1,word2)
    print(res)


