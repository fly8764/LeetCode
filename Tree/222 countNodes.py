# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        #简单做法，BFS 统计个数
        if not root:
            return 0
        cnt = 0
        parent = [root]
        # 这里可尝试 不用while，直接迭代遍历parent，可以，但是比较慢
        while parent:
            node = parent.pop(0)
            cnt += 1
            if node.left:
                parent.append(node.left)
            if node.right:
                parent.append(node.right)
        return cnt

    # def countNodes(self, root):
    #     #简单做法，BFS 统计个数
    #     if not root:
    #         return 0
    #     cnt = 0
    #     parent = [root]
    #     while parent:
    #         #这里可尝试 不用while，直接迭代遍历parent
    #         cur = []
    #         for node in parent:
    #             cnt += 1
    #             if node.left:
    #                 cur.append(node.left)
    #             if node.right:
    #                 cur.append(node.right)
    #         parent = cur[:]
    #     return cnt


