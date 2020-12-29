# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

'''
2020/12/8 1:19
深度优先搜索 递归
'''
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)

        return max(depth_l,depth_r) + 1


