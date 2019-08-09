# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.dia = 0

    def find(self,root):
        if not root:
            return 0
        left_h = self.find(root.left)
        right_h = self.find(root.right)
        self.dia = max(self.dia,left_h+ right_h)
        return max(left_h,right_h)+1

    def diameterOfBinaryTree(self, root):
        #递归
        if not root:
            return 0
        self.find(root)

        return self.dia


    def depth(self,root):
        if not root:
            return 0
        parent = [root]
        cnt = 0
        while parent:
            cur = []
            cnt += 1
            for node in parent:
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            parent = cur[:]
        return cnt


    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dia = 0
        if not root:
            return dia

        parent = [root]
        while parent:
            cur = []
            for node in parent:
                left_h,right_h = 0,0
                if node.left:
                    cur.append(node.left)
                    left_h = self.depth(node.left)
                if node.right:
                    cur.append(node.right)
                    right_h = self.depth(node.right)
                dia = max(dia,left_h+right_h)
            parent = cur[:]
        return dia


