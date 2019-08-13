# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        self.res = 0
        if not root:
            return 0

        def dfs(root):
            if not root.left and not root.right:
                return 0

            temp_left,temp_right = 0,0
            if root.left:
                left = dfs(root.left)
                if root.val == root.left.val:
                    temp_left = left + 1

            if root.right:
                right =dfs(root.right)
                if root.val == root.right.val:
                    temp_right = right + 1
            self.res = max(self.res,temp_left + temp_right)
            return max(temp_left,temp_right)

        dfs(root)
        return self.res
