"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        depth = 0

        parent = [root]
        while parent:
            depth += 1
            child = []
            for _ in range(len(parent)):
                node = parent.pop(0)
                if node.children:
                    child.extend(node.children)
            parent = child[:]

        return depth

