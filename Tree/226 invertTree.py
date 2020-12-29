# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
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

'''
2020/12/11 22:41

方法一 递归 从上到下
第二次做没做出来，整体的递归逻辑没有想清楚。
就像两个变量交换值一样，对于树是同样的操作，可以直接把一个节点赋值给一个变量。

方法二 递归 从下到上
从上到下 每遇到一个节点，都先把其左右节点交换好，然后再递归下去，继续交换。
'''
class Solution:
    def invertTree1(self, root):
        if not root:
            return
        def dfs(root):
            if not root:
                return

            temp = root.left
            root.left = dfs(root.right)
            root.right = dfs(temp)

            return root
        root = dfs(root)
        return root

    def invertTree(self, root):
        if not root:
            return

        if root.left:
            node = TreeNode(root.left.val)
            node.left = root.left.left
            node.right = root.left.right
        else:
            node = None

        root.left = root.right
        root.right = node
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root






