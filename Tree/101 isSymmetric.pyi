# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
方法一：迭代
1、使用一个队列，每次把位置上对称的两个节点一块放在队尾，
2、每次从队首取出两个元素，判读是否相等(这里根据是否为空节点，有四种情况，先排除简单的
都为空节点，接下还有三种情况，只有一个空节点(两种)，没有空节点，有了之前的判读排除，
接下来就不会纠结，考虑那么多了（第二次练习时就在这犯难了））
3、每次往队尾加入元素时，按照对称顺序加入（重点）

方法二：递归 从上到下
在递归函数的基础上做，mirror(left,right)
用来判断分别以left 和right为根的两棵子树是否对称，
mirror内部，判读根是否相等，根和上面迭代法一样，有四种情况，逐渐排除，减少考虑的范围
然后判读对称位置的子树是否相等
'''
class Solution1:
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


