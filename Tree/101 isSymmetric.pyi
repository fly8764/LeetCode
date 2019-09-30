# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #左右子树按照相反的顺序先序遍历，不对
    # [1,2,2,null,3,null,3]
    #遇到 空节点，res后接None，也不行，……
    def preOrderLeft(self,root):
        res = []
        if not root: return res
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            if not node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                else:
                    stack.append(None)
                if node.left:
                    stack.append(node.left)
                else:
                    stack.append(None)
            else:
                res.append(None)
        return res

    def preOrderRight(self,root):
        res = []
        if not root: return res
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            if not node:
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                else:stack.append(None)
                if node.right:
                    stack.append(node.right)
                else:stack.append(None)
            else:
                res.append(None)
            # res.append(node.val)
            # if node.left:
            #     stack.append(node.left)
            # if node.right:
            #     stack.append(node.right)
        return res

    def isSymmetric(self, root):
        if not root:return True
        left = self.preOrderLeft(root)
        print(left)
        right = self.preOrderRight(root)
        if left == right:
            return True
        else:
            return False

class Solution:
    #递归
    def isSymmetric1(self,root):
        queue = [root,root]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            #别忘了判断边界条件
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True

    def mirros(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.mirros(left.left,right.right) and self.mirros(left.right,right.left)

    def isSymmetric(self,root):
        res= self.mirros(root,root)
        if res:return True
        else:return False


