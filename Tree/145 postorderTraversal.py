# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal2(self, root):
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

    def postorderTraversal3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        if root.left:
            res += self.postorderTraversal(root.left)
        if root.right:
            res += self.postorderTraversal(root.right)
        res += [root.val]

        return res

    def postorder(self,root):
        res,stack = [],[]
        p = root
        while stack:
            res.append(p.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
            if not stack:
                p = stack.pop()

        return res[::-1]

    def postorder2(self,root):
        res = []
        stack = [root] if root else []
        while stack:
            # 前序遍历 访问左右节点的顺序改变一下
            # 最后，把得到的res，再反转一下
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

    def postorderTraversal(self, root):
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
