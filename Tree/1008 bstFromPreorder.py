# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        # 递归 找到左右子树的先序序列，然后递归的去构造子树，并赋值给 root的左右节点。
        if not preorder:
            return
        # 这里要注意，right 初始化为最后一位，避免没有右子树
        right = len(preorder)
        for i in range(1,len(preorder)):
            if preorder[i] > preorder[0]:
                right = i
                break

        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder(preorder[1:right])
        root.right = self.bstFromPreorder(preorder[right:])

        return root


