# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def dfs(self,root):
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.ret += root.left.val
        self.dfs(root.left)
        self.dfs(root.right)

    def sumOfLeftLeaves(self, root):
        self.dfs(root)
        return self.ret


    # def sumOfLeftLeaves(self, root):
    #     if not root:
    #         return 0
    #
    #     ret = 0
    #     parent= [[root.left,root.right]]
    #     while parent:
    #         cur = []
    #         for node in parent:
    #             left,right = node[0],node[1]
    #             if left and (not left.left and not left.right):
    #                 ret += left.val
    #
    #             if left:
    #                 cur.append([left.left,left.right])
    #             if right:
    #                 cur.append([right.left, right.right])
    #         parent = cur[:]
    #     return ret






