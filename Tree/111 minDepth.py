# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        depth = 0

        parent = [root]
        flag = False

        while parent:
            depth += 1
            child = []
            for _ in range(len(parent)):
                node = parent.pop(0)
                if not node.left and not node.right:
                     flag = True

                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            if flag:
                return depth

            parent = child[:]

        return depth

