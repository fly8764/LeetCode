# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        parent = [root]

        while parent:
            child = []
            cur = []
            for _ in range(len(parent)):
                node = parent.pop(0)
                cur.append(node.val)
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)

            res.append(cur)
            parent = child[:]

        return res



