# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        stack,res = [],[]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if not root:
    #         return []
    #     res = []
    #     if root.left:
    #         res += self.postorderTraversal(root.left)
    #     if root.right:
    #         res += self.postorderTraversal(root.right)
    #     res += [root.val]
    #
    #     return res

