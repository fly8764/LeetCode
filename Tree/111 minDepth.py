# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
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


'''
2020/12/10 18:41
方法一 递归
深度：根节点到最近一个叶子节点的路径上的节点树，重点是叶子节点。
对应极端的一条路径到底的，结果不是1，而是那条路径的长度。要考虑到这种情况。
所以要分情况讨论，尤其是其中一个孩子节点为空的非叶子节点。
'''
class Solution:
    # 没考虑极端情况
    def minDepth1(self, root):
        def dfs(root):
            if not root:
                return 0
            d_f = dfs(root.left)
            d_r = dfs(root.right)
            return min(d_f,d_r) + 1
        return dfs(root)

    # 这种写法非常耗时，可以适当添加剪枝函数
    def minDepth2(self, root):
        if not root:
            return 0
        left = self.minDepth2(root.left)
        right = self.minDepth2(root.right)
        if root.left and root.right:
            return 1 + min(left,right)
        else:
            return 1 + max(left,right)

    # 增加剪枝函数，对左右孩子节点是否为空，四种情况分类讨论,
    # 好像时间差不多……
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))



