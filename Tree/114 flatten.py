# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#方法一：先序遍历 找到对应节点，同时把节点串接在 上个节点右节点上
class Solution:
    # def flatten(self, root):
    #     #一边遍历，一边修改节点
    #     if not root:
    #         return

    def flatten(self, root):
        if not root:
            return
        pre = None
        def dfs(root):
            if not root:
                return
            if pre:
                pre.right,pre.left = root,None
            pre = root
            right = root.right
            pre.right = root



    # def flatten(self, root):
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if not root:
    #         return
    #     # node = TreeNode(0)
    #     # ret = node
    #     res = root
    #     # res.left = None
    #     root2 = root
    #     def dfs(root,ret):
    #         # res = []
    #         stack = []
    #         while True:
    #             while root:
    #                 temp = TreeNode(root.val)
    #                 ret.right = temp
    #                 ret = temp
    #                 # res.append(root.val)
    #                 stack.append(root.right)
    #                 root = root.left
    #             if not stack:
    #                 return
    #             root = stack.pop()
    #     dfs(root2,res)
    #     root.left = None
        # return node.right

        # res = dfs(root)
        # root.left = None
        # temp = root
        # for item in res[1:]:
        #     node = TreeNode(item)
        #     temp.right = node
        #     temp = node

    # def flatten(self, root):
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if not root:
    #         return
    #
    #     def dfs(root):
    #         res = []
    #         stack = []
    #         while True:
    #             while root:
    #                 res.append(root.val)
    #                 stack.append(root.right)
    #                 root = root.left
    #             if not stack:
    #                return res
    #             root = stack.pop()
    #     res = dfs(root)
    #     root.left = None
    #     temp = root
    #     for item in res[1:]:
    #         node = TreeNode(item)
    #         temp.right = node
    #         temp = node





