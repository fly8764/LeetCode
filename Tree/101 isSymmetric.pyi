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

class Solution2:
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

'''
2020/12/7 23:09
方法一 迭代（递推）
迭代其实相当于一种递推（重点），在上一次已满足条件的情况下，去判断下一次。
在一个队列中取出两个对称的节点，去判断其孩子节点是否对称，即left.left == right.right  left.right == right.left
每次把位置对称的两个节点放到队尾，这样下一次迭代时，从队首取出的两个节点才能继续往下判断是否对称。
考虑到空接点，要分四种情况讨论，都为空节点，有一个是空节点，都不是空节点。其中都为空节点的，continue继续下一次迭代
递归的起始状态：[root,root] 这一点不好想到

方法二 递归
类似于方法一
框架：
left.left == right.right  left.right == right.left
递归函数的起始判断条件，依然是那四种情况，进行讨论。
其中在left.val == right.val时，要使用递归继续判断。

感悟：
树的题目要结合树的结构特点。
'''
class Solution:
    # 超时
    def isSymmetric1(self,root):
        if not root:
            return True
        res = []
        parent = [root]
        while parent:
            tem_res = []
            child = []
            for node in parent:
                if node:
                    tem_res.append(node.val)
                else:
                    tem_res.append(None)
                if node.left:
                    child.append(node.left)
                else:
                    child.append(None)
                if node.right:
                    child.append(node.right)
                else:
                    child.append(None)
            if tem_res != tem_res[::-1]:
                return False

        return True

    def isSymmetric2(self, root):
        if not root:
            return True
        queue = [root,root]

        while queue:
            left = queue.pop(0)
            right = queue.pop(0)

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.extend([left.left,right.right])
            queue.extend([left.right,right.left])

        return True

    def mirror(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)


    def isSymmetric(self, root):
        if not root:
            return True
        return self.mirror(root,root)








