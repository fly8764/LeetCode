# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res,stack = [],[]
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            temp = stack.pop()
            res.append(temp.val)
            #开始关注右子树
            p = temp.right
        return res

    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     res = []
    #     if not root:
    #         return res
    #     if root.left:
    #         res.extend(self.inorderTraversal(root.left))
    #     res.append(root.val)
    #     if root.right:
    #         res.extend(self.inorderTraversal(root.right))
    #     return res


