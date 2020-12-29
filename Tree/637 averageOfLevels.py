# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def averageOfLevels(self, root) :
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
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)

            res.append(sum(cur)/len(cur))
            parent = child[:]

        return res

'''
2020/12/7 22:45
'''
class Solution:
    def averageOfLevels(self, root) :
        if not root:
            return []

        res = []
        parent = [root]
        while parent:
            tmp_res = []
            children = []
            for node in parent:
                tmp_res.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            res.append(sum(tmp_res)/len(tmp_res))
            parent = children[:]
        return res

