
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        res = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res


    # def preorder(self, root):
    #     if not root:
    #         return []
    #
    #     res = [root.val]
    #     children = root.children
    #     if  children:
    #         for child in children:
    #             res += self.preorder(child)
    #     return res

