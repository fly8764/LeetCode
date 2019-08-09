# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if root.right:
            self.convertBST(root.right)
            if root.right.left:#这个是root 右子树中的最小节点
                root.val += root.right.left.val
            else:
                root.val += root.right.val

        if root.left:
            # root.left.val += root.val
            if root.left.right:
                #这个是root左子树中的最大值，仅次于root，要把root的值加到其左子树的最大值中，如何加过取去
                root.left.right.val += root.val
            else:#
                root.left.val += root.val
            self.convertBST(root.left)
        return root

