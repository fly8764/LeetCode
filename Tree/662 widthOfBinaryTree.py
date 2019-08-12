# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 根据二叉树的性质，
# 按照满二叉树的模板，记录 每一层从左到右，每个节点对应的序号（1，……，2×N）
# 每个节点i，其左右孩子节点，在对应的孩子层，其序号为(2×i-1,2×i)
# 每次迭代记录节点和对应的序号即可。

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        parent = [root]
        idx = [1]
        width = 0

        while parent:
            width = max(width,idx[-1] - idx[0] + 1)
            cur = []
            new_id = []
            for i in range(len(parent)):
                node = parent[i]
                if node.left:
                    cur.append(node.left)
                    new_id.append(2*idx[i]-1)
                if node.right:
                    cur.append(node.right)
                    new_id.append(2*idx[i])

            parent = cur[:]
            idx = new_id[:]
        return width




