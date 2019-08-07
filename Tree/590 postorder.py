"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root):
        pass

    # def postorder(self, root):
    #     if not root:
    #         return []
    #     res = []
    #     # 这里要先判断 root是否有孩子节点;类似于之前判断左右节点一样
    #     if root.children:
    #         for child in root.children:
    #             res += self.postorder(child)
    #     res += [root.val]
    #     return res