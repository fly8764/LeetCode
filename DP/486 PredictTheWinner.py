'''
给定一个表示分数的非负整数数组。 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，
然后玩家1拿，……。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。
最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1:

输入: [1, 5, 2]
输出: False
解释: 一开始，玩家1可以从1和2中进行选择。
如果他选择2（或者1），那么玩家2可以从1（或者2）和5中进行选择。如果玩家2选择了5，那么玩家1则只剩下1（或者2）可选。
所以，玩家1的最终分数为 1 + 2 = 3，而玩家2为 5。
因此，玩家1永远不会成为赢家，返回 False。
示例 2:

输入: [1, 5, 233, 7]
输出: True
解释: 玩家1一开始选择1。然后玩家2必须从5和7中进行选择。无论玩家2选择了哪个，玩家1都可以选择233。
最终，玩家1（234分）比玩家2（12分）获得更多的分数，所以返回 True，表示玩家1可以成为赢家。
注意:

1 <= 给定的数组长度 <= 20.
数组里所有分数都为非负数且不会大于10000000。
如果最终两个玩家的分数相等，那么玩家1仍为赢家。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/predict-the-winner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
选手A，B，A是先手
当数值个数 size为偶数时，先手可以选择 奇数列 和偶数列中的较大者，每次只取奇数或者偶数列即可
每次当先手 取奇数列后，后手只能取偶数列，下一次，依然如此，两人只能取一种列，并且有先手决定；
只要先手 坚持选择较大的那个列(只取奇数或偶数列)，一定能够胜出；中途也可以换，但坚持一定可以的；

对于奇数，就比较麻烦了，每次都会动态变化，先手上来只能取奇数列，后手 可以取 奇偶列；后手的每个决定都会
影响后面的操作，所以，上面偶数的解法行不通了。
dp[i][j]:表示nums[i:j+1]序列 先手比后手多出来的分数；
nums[i:j+1]:对于两端的值，当先手A取nums[i]时，nums[i+1:j+1]中 A就不是先手了，B是先手了，因为A先取了nums[i];
所以要比较先手A的优势nums[i] 和B在 nums[i+1:j+1]的优势dp[i+1][j]，做差比较 nums[i] - dp[i+1][j]
同理，当A取nums[ｊ]时，nums[i:j]中 A就不是先后了，B是先手了，比较优势 nums[j] - dp[i][j-1]
最终 dp[i][j] = max(nums[i] - dp[i+1][j],nums[j] - dp[i][j-1]),nums[i:j+1]范围内，先手的优势
'''
#左边界l 从右往左；右边界从l+1到n；整体上 从右往左进行遍历循环
class Solution:
    # def PredictTheWinner(self, nums):
    #     size = len(nums)
    #     if size %2 == 0 or size == 1:
    #         return True
    #     dp = [[0]*size for _ in range(size)]
    #     for i in range(size-1,-1,-1):
    #         dp[i][i] = nums[i]
    #         for j in range(i+1,size):
    #             dp[i][j] = max(nums[i]- dp[i+1][j],nums[j] -dp[i][j-1])
    #
    #     return dp[0][-1] >=0

    def PredictTheWinner(self, nums):
        size = len(nums)
        if size %2 == 0 or size == 1:
            return True

        dp = [0]*size
        for i in range(size-1,-1,-1):
            dp[i] = nums[i]
            for j in range(i+1,size):
                dp[j] = max(nums[i]- dp[j],nums[j]-dp[j-1])

        #整体上是从右往左，但是最终判断时是 dp[-1]而不是dp[0]
        #第i层循环时，一维的dp[j]代表从i到j，先手比后手 多得到分数；
        #当从后往前 循环 n层时，dp[-1]代表 从整个序列，先手比后手 多得的分数
        return dp[-1] >= 0


if __name__ == '__main__':
    so = Solution()
    nums = [1, 5, 2]
    res = so.PredictTheWinner(nums)
    print(res)

