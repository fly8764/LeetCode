# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #返回子树，直接返回子树的根节点即可，不用遍历子树
    def searchBST0(self, root, val):
        #直接遍历
        while root:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right

    def searchBST(self, root, val):
        #递归
        if not root:
            return None

        if root.val == val:
            return root
        if root.val > val:
            return  self.searchBST(root.left,val)
        else:
            return  self.searchBST(root.right,val)





