# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#当使用常规方法时，要注意 除了最上面的根节点满足平衡外，还要判断其左右子树是否满足平衡(重点)
#牛客网 的测试用例，没有考虑 后面的重点，
class Solution:
    # def depth(self,root):
    #     if not root:return 0
    #
    #     left = self.depth(root.left)
    #     if left == -1:return -1
    #     right = self.depth(root.right)
    #     if right == -1:return -1
    #
    #     if abs(left - right) < 2:
    #         return max(left,right)+1
    #     else:
    #         return -1
    #
    #
    # def IsBalanced_Solution(self, pRoot):
    #     res = self.depth(pRoot)
    #
    #     return res != -1

    def depth(self,root):
        if not root:return 0
        left = self.depth(root.left)
        right = self.depth(root.right)

        return max(left,right) + 1

    def IsBalanced_Solution(self, pRoot):
        if not pRoot:return True

        left = self.depth(pRoot.left)
        right = self.depth(pRoot.right)

        # 这种方式 使得 递归地判断 每个子树是否满足平衡，很好
        if abs(left - right) < 2 and self.IsBalanced_Solution(pRoot.left) \
                and self.IsBalanced_Solution(pRoot.right):
            return True
        else:
            return False

