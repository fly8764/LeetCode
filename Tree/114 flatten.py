# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        if not root:
            return
        pre = None
        stack = []

        while True:
            while root:
                if pre:
                    pre.right,pre.left = root,None
                pre = root
                stack.append(root.right)
                root = root.left
            if not stack:
                return
            root = stack.pop()


    # def flatten(self, root):
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     self.pre = None
    #
    #     def dfs(root):
    #         if not root:
    #             return
    #         if self.pre:
    #             self.pre.right,self.pre.left = root,None
    #         right = root.right
    #         self.pre = root
    #         dfs(root.left)
    #         dfs(right)
    #
    #     dfs(root)


