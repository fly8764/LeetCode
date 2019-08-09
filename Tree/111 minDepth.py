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
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right)+1
        if not root.right:
            return self.minDepth(root.left)+1
        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))

    # def minDepth(self, root):
    #     if not root:
    #         return 0
    #     depth = 0
    #
    #     parent = [root]
    #     flag = False
    #
    #     while parent:
    #         depth += 1
    #         child = []
    #         for _ in range(len(parent)):
    #             node = parent.pop(0)
    #             if not node.left and not node.right:
    #                  flag = True
    #
    #             if node.left:
    #                 child.append(node.left)
    #             if node.right:
    #                 child.append(node.right)
    #         if flag:
    #             return depth
    #
    #         parent = child[:]
    #
    #     return depth

