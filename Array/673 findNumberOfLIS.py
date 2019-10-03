class Solution:
    def findNumberOfLIS1(self, nums):
        size = len(nums)
        if size < 2:return size
        # dic = {}
        cnt = 1
        maxx = 1
        res = 0
        for i in range(1,size):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                # if cnt not in dic:
                #     dic[cnt] = 1
                # else:
                #     dic[cnt] += 1
                cnt = 1
            if cnt > maxx:
                maxx = cnt
                res = 1
            elif cnt == maxx:
                res += 1
            # maxx = max(maxx,cnt)
        return res

    def findNumberOfLIS(self, nums):
        size = len(nums)
        dp = [1]*size
        cnt = [1]*size
        maxx = 1
        res = 0
        # lis = [[] for _ in range(size)]
        # lis[0].append(nums[0])
        for i in range(1,size):
            for j in range(i):
                if nums[i] > nums[j]:
                    # dp[i] = max(dp[i],dp[j]+1)
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j]+1:
                        cnt[i] += 1
                    #     dp[i] = dp[j] + 1
                    #     temp = lis[j] + [nums[i]]
                    #     lis[i] = [temp]
                    # elif dp[i] == dp[j]+1:
                    #     new = lis[j]+ [nums[i]]
                    #     lis[i].append(new)

            if dp[i] > maxx:
                maxx = dp[i]
                res = cnt[i]
            elif dp[i] == maxx:
                res += 1
                # res.extend(lis[i])
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [1,3,5,4,7]
    print(so.findNumberOfLIS(nums))
    nums = [2]*5
    print(so.findNumberOfLIS(nums))

