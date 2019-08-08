# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def depth(self,root):
    #     #递归  这个递归方法返回的深度 是包括根节点的
    #     if not root:
    #         return 0
    #     left_h = self.depth(root.left)
    #     right_h = self.depth(root.right)
    #     return max(left_h,right_h)+1


    def depth(self,root):
        #BFS
        if not root:
            return 0
        parent = [root]
        cnt = 0
        while parent:
            cnt += 1
            cur = []
            for node in parent:
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            parent = cur[:]
        return cnt

    def diameterOfBinaryTree(self, root):
        #使用递归来做
        if not root:
            return 0
        left_h = 0
        right_h = 0
        if root.left:
            left_h = self.depth(root.left)
        if root.right:
            right_h = self.depth(root.right)

        return  left_h + right_h

