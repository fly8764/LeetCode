# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS(后序遍历) + 回溯
#这题是 二叉搜索树，可以利用其性质，只在根节点的一个子树上递归，即剪枝
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        #迭代法, 比递归法 少了一些出栈，递归中当找到公共节点时，其实可以不用
        #停止递归，出栈，但是还需要出栈，
        if p.val > q.val:
            p,q = q,p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                return root



    # def lowestCommonAncestor(self, root, p, q):
    #     self.res = None
    #     def dfs(root,p,q):
    #         if not root:
    #             return 0
    #
    #         left,right = 0,0
    #         if root.val >p.val and root.val > q.val:
    #             left = dfs(root.left,p,q)
    #         elif root.val < p.val and root.val < q.val :
    #             right = dfs(root.right, p, q)
    #         else:
    #             left = dfs(root.left,p,q)
    #             right = dfs(root.right,p,q)
    #         mid = root == p or root == q
    #
    #         if left + right + mid > 1:
    #             self.res = root
    #         return left or right or mid
    #     dfs(root,p,q)
    #     return self.res

    # def lowestCommonAncestor(self, root, p, q):
    #     self.res = None
    #
    #     def dfs(root,p,q):
    #         if not root:
    #             return 0
    #         left = dfs(root.left,p,q)
    #         right = dfs(root.right,p,q)
    #         mid = root == p or root == q
    #         if mid + left + right > 1:
    #             self.res = root
    #         return left or right or mid
    #
    #     dfs(root,p,q)
    #     return self.res

