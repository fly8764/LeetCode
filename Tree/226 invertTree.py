# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #镜像对称，直接把每个节点的左右节点对换即可
    # def invertTree(self, root):
    #     #从下到上
    #     if not root:
    #         return
    #     #python 不用预定义变量，可以根据赋值变量来定义类型
    #     temp = root.left
    #     root.left = self.invertTree(root.right)
    #     root.right = self.invertTree(temp)
    #     return root

    def invertTree(self, root):
        #从上到下
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            if root.left:
                temp = TreeNode(root.left.val)
                temp.left = root.left.left
                temp.right = root.left.right
            else:
                temp = None

            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

