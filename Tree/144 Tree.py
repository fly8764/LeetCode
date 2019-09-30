# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        res, stack = [],[]
        while True:
            # if root:
            #从右往左 把节点入栈,这种写法 看着明了，在N叉树中体现的很重要
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            res.append(root.val)

            if not stack:
                return res
            root = stack.pop()


    # def preorderTraversal(self, root):
    #     res,stack = [],[]
    #     while True:
    #         while root:
    #             #不断地前序遍历，直到左节点为none，
    #             #只把右节点往栈往里面不断地加，所以出栈的都是原先的右节点
    #             res.append(root.val)
    #             stack.append(root.right)
    #             root = root.left
    #
    #         if not stack:
    #             return res
    #         root = stack.pop()

    # def preorderTraversal(self, root):
    #     if not root:
    #         return []
    #     res = []
    #     res += [root.val]
    #     res += self.preorderTraversal(root.left)
    #     res += self.preorderTraversal(root.right)
    #     return res

class Solution2:
    def preorder(self,root):
        if not root:return []
        res = []
        stack = []
        while True:
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

            if not stack:
                return res
            root = stack.pop()

class Solution3:
    def preorder(self,root):
        if not root:return []
        res,stack = [],[]
        node = root
        while stack:
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if not stack:
                return res

            node = stack.pop()




