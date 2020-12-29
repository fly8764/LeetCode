# 标签：动态规划
# 假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
# G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
#
# 当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
# f(i) = G(i-1)*G(n-i)
#
# 综合两个公式可以得到 卡特兰数 公式
# G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
# 
# 作者：guanpengchn
# 链接：https://leetcode-cn.com/problems/two-sum/solution/hua-jie-suan-fa-96-bu-tong-de-er-cha-sou-suo-shu-b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution1:
    def numTrees(self, n: int):
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]

'''
2020/12/7 20:56
动态规划 一维数组
找出递归公式
f(i)代表以i为根节点的二叉搜索树的个数
G(n)代表以{1,2,...,n}为节点组成的二叉搜索树的种类数，则
G(n) = f(1) + f(2) + f(3) + ... + f(n)
当i为根节点时，其左子树的节点树为i-1，右子树的节点数为n-i
f(i) = G(i-1) + G(n-i)
综上，得到 卡特兰公式
G(n) = G(0)G(n-1) + G(1)G(n-2) + G(2)G(n-3) + ... + G(n-1)G(0)
'''
class Solution:
    def numTrees(self, n):
        dp = [0] * (1+n)
        dp[0] = dp[1] = 1

        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]

        return dp[n]


if __name__ == '__main__':
    so = Solution()
    res = so.numTrees(3)
    print(res)

