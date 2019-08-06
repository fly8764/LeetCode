# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self,root):
        #自下而上，发现不平衡的节点后，直接返回-1，不用再接着遍历下去
        if not root:
            return 0

        left = self.depth(root.left)
        if left == -1:return -1
        right = self.depth(root.right)
        if right == -1: return -1

        return max(left,right)+1 if abs(left- right)<2 else -1

    def isBalanced(self, root):
        return self.depth(root) != -1


    # def depth(self,root):
    #     if not root:
    #         return 0
    #     left_h = self.depth(root.left)
    #     right_h = self.depth(root.right)
    #     return max(left_h,right_h)+1

    # def isBalanced(self,root):
    #     #自顶而下，要求顶点root 和 左右两个子节点也满足平衡(重点)
    #     if not root:
    #         return True
    #     left_h = self.depth(root.left)
    #     right_h = self.depth(root.right)
    #
    #     return abs(left_h - right_h) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
