# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#这种方法 是 从底往上 递归
#DFS(后序遍历) + 回溯法(现在认为回溯法就是 DFS在递归时 剪枝，返回)，本体是回溯 mid
#当left,right,mid有两个为True时，结果就可以一定是 root.val
#每次递归返回 当前有没有找到p or q，返回给上层 递归看
#注意 题目中给的p，q是树节点，而不是值

#测试
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.res = None
        self.dfs(root,p,q)
        return self.res

    def dfs(self,root,p,q):
        if not root:
            return 0

        left = self.dfs(root.left,p,q)
        right = self.dfs(root.right,p,q)
        mid = root == p or root == q
        if left + right + mid > 1:
            self.res = root
        return left or right or mid

