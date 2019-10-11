'''
最长公共子数组：要求连续
最长公共子串：不要求连续
两种问题，在字符串相等时，动态转移方程相同，dp[i][j] = dp[i-1][j-1]+1
在不等式不同，
最长公共子数组：dp[i][j] = 0，因为连续，所以一旦不等就中断，
最长公共子串：dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 不连续，所以还可以连续继续用，
最终返回的结果也不同，
最长公共子数组：max(max(row) for row in dp) 因为dp[i][j]代表以当前位置为尾的公共子数组，
所以最终要遍历取最大值
最长公共子串：dp[-1][-1]，dp[i][j]代表 到目前位置的最大长度，可以不连续，所以状态可以延续
上面的公共子数组，就不能把状态直接延续下去

'''
class Solution:
    def findLength(self, nums1, nums2):
        size1 = len(nums1)
        size2 = len(nums2)
        res = 0
        dp = [[0]*(size2+1) for i in range(size1+1)]
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    #注意在不相等时，动态转移方程的写法
                    #分别是最长公共子数组和 最长公共子串
                    #dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    dp[i][j] = 0
                # res = max(res,dp[i][j])
        #两种写法的最终返回方式也不同，最长公共子数组的结果也可以在比较中不断更新
        # return dp[-1][-1]
        #最终一次性比较找最大值的方式比较快
        return max(max(row) for row in dp)
        # return res


if __name__ == "__main__":
    so = Solution()
    print(so.findLength([1,2,3,2,1], [3,2,1,4,7]))
    print(so.findLength([0,1,1,1,1],[1,0,1,0,1]))