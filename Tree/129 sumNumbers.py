# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        res = []
        def dfs(root,ans):
            new_ans = ans*10 + root.val
            if not root.left and not root.right:
                res.append(new_ans)
            if root.left:
                dfs(root.left,new_ans)
            if root.right:
                dfs(root.right,new_ans)
        dfs(root,0)
        return sum(res)


