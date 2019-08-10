# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def smallestFromLeaf(self, root):
        self.ans = "~"

        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(A)))

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop() #防止此次递归出去后，A影响到下一个递归，后面的操作

        dfs(root, [])
        return self.ans

    # def smallestFromLeaf(self, root):
    #     if not root:
    #         return
    #     res = []
    #     def dfs(root,cur):
    #         new_cur = chr(ord('a')+root.val) + cur
    #         if not root.left and not root.right:
    #             res.append(new_cur)
    #         if root.left:
    #             dfs(root.left,new_cur)
    #         if root.right:
    #             dfs(root.right,new_cur)
    #     dfs(root,'')
    #     return min(res)

    # def smallestFromLeaf(self, root):
    #     if not root:
    #         return
    #     res = []
    #     def dfs(root,cur):
    #         new_cur = chr(ord('a')+root.val) + cur
    #         if not root.left and not root.right:
    #             res.append(new_cur)
    #         if root.left:
    #             dfs(root.left,new_cur)
    #         if root.right:
    #             dfs(root.right,new_cur)
    #     dfs(root,'')
    #     return min(res)


    # def smallestFromLeaf(self, root):
    #     #python min()可以直接判断 字符串的大小，因此不用考虑如何判断字符串的字典序
    #     """
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     a = 'abcdefghijklmnopqrstuvwxyz'
    #     if not root:
    #         return
    #     res = '~'
    #     def dfs(root,cur):
    #         if not root.left and not root.right:
    #             nonlocal res
    #             res = min(res,a[root.val] + cur)
    #         if root.left:
    #             dfs(root.left,a[root.val]+cur)
    #         if root.right:
    #             dfs(root.right,a[root.val]+cur)
    #
    #     dfs(root,'')
    #     return res





