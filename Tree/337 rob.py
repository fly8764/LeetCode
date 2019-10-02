# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 二叉树的性质，考虑**左右子树**两个方向；
# 数组，对应一维，只考虑一个方向；dp[i] = max(dp[i-2]+nums[i],dp[i-1]);
#
# dp[0],dp[1] 分别表示不选该节点 和选择该节点的情况。
# 1.当选择根节点时，不能选择其孩子节点，对应root.val + l[0] + r[0]
# 2.当不选择根节点时，是不是就一定要选择其对对应的孩子节点呢？
# 不一定，当孩子节点值为1，孩子的的左右节点均为100时，显然不选孩子节点，对应
# l[0]+r[0], 此时，不选根节点 也不选根节点对应的孩子节点，那加上根节点不更大，是的，此时就是 加上根节点的情况 root.val + l[0] + r[0]
# 当不选根节点时，左右节点都不一定一定要取，当取左时，右边可取可不取；当不取右边时，貌似可以加根，但是左边不允许；
# 所以，对于不取根，应该返回 max(l) + max(r);

class Solution1:
    #树上动态规划
    # 当不选根节点时，左右节点都不一定一定要取
    def rob(self, root):
        def dfs(root):
            if not root:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            return [max(left)+max(right),root.val + left[0] + right[0]]
        res = dfs(root)

        return max(res)

'''
对于每颗数，其根节点可选，可不选
设置res[0],res[1] 分别代表不选和选，
选择了根节点，则不能选择直接孩子节点，即root.val+left[0]+right[0]
不选，则孩子节点及孙子节点，可选可不选，按照最大来选即可，
因为，有时孙子节点比孩子节点还大，如果选择了孩子节点，那么孙子节点就不能选了
'''
class Solution:
    def dfs1(self,root):
        #这种方法不对
        #错在，认为不选根节点，那么孩子节点一定要选取，这就有些死板，动态的意思不强
        #孩子节点不一定选取，选择了孩子节点，孙子节点就没法选取，有时孙子节点比孩子节点还大
        if not root:
            return 0
        child  = root.val
        temp = 0
        if root.left:
            temp += root.left.val
            if root.left.left:
                child += self.dfs(root.left.left)
            if root.left.right:
                child += self.dfs(root.left.right)
        if root.right:
            temp += root.right.val
            if root.right.left:
                child += self.dfs(root.right.left)
            if root.right.right:
                child += self.dfs(root.right.right)
        return max(child,temp)

        # return max(root.val,self.dfs(root.left.left)+self.dfs(root.left.right)+
        #                     self.dfs(root.right.left)+self.dfs(root.right.right))

    def dfs(self,root):
        if not root:
            return [0,0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return [max(left)+max(right),root.val+left[0]+right[0]]

    def rob(self,root):
        res = self.dfs(root)
        return max(res)
