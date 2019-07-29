# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        #BFS
        if not pRoot:
            return 0
        parent = [pRoot]
        cur = []
        depth = 0

        while parent:
            depth += 1
            cur = []
            for _ in range(len(parent)):
                item = parent.pop(0)
                if item.left:
                    cur.append(item.left)
                if item.right:
                    cur.append(item.right)
            parent = cur[:]
        return depth