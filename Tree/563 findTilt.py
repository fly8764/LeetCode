# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        if not root:
            return 0
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left-right)
            return left+ right + root.val

        dfs(root)
        return self.res



