"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        parent = [root]

        while parent:
            child = []
            cur = []
            for _ in range(len(parent)):
                node = parent.pop(0)
                cur.append(node.val)
                if node.children:
                    child.extend(node.children)

            res.append(cur)
            parent = child[:]

        return res
