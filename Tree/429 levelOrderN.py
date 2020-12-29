"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution1:
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

'''
2020/12/7 22:40
node.children是个列表，需要注意
'''
class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        parent = [root]

        while parent:
            children = []
            tmp_res = []
            # 有两种遍历方式
            for node in parent:
            # for _ in range(len(parent)):
            #     node = parent.pop(0)
                tmp_res.append(node.val)
                if node.children:
                    children.extend(node.children[:])

            res.append(tmp_res)
            parent = children[:]
        return res