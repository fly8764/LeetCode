# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自顶而下，要求顶点root 和 左右两个子节点也满足平衡(重点)
class Solution1:
    def depth(self,root):
        #自下而上，一旦发现不平衡的节点后，直接返回-1，按照出栈顺序，一路返回-1
        #不会遍历另一棵子树
        if not root:
            return 0

        left = self.depth(root.left)
        if left == -1:return -1
        right = self.depth(root.right)
        if right == -1: return -1

        return max(left,right)+1 if abs(left- right)<2 else -1

    def isBalanced(self, root):
        return self.depth(root) != -1


    # def depth(self,root):
    #比较自然的想法；会遍历所有的子树
    #     if not root:
    #         return 0
    #     left_h = self.depth(root.left)
    #     right_h = self.depth(root.right)
    #     return max(left_h,right_h)+1

    # def isBalanced(self,root):
    #     #自顶而下，要求顶点root 和 左右两个子节点也满足平衡(重点)
    #     if not root:
    #         return True
    #     left_h = self.depth(root.left)
    #     right_h = self.depth(root.right)
    #     #这种方式 使得 递归地判断 每个子树是否满足平衡，很好
    #     return abs(left_h - right_h) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

'''
2020/12/10 17:18
递归 dfs
平衡：左右子树平衡 + 该节点平衡
每次递归要查看该节点左右子树是否均平衡，同时要返回左右子树的最大高度，判断该节点是否平衡。
第二次做该题时，递归返回两个值，是否平衡和其子树的最大高度；其实也可以返回一个，如果子树不平衡，
直接返回结果False，不要再返回其左右子树的高度了。
'''
class Solution:
    def depth(self,root):
        if not root:
            return True,0
        res_l,d_l = self.depth(root.left)
        res_r,d_r = self.depth(root.right)

        if res_l and res_r and abs(d_l - d_r) <= 1:
            return True,max(d_l,d_r) + 1
        else:
            return False,max(d_l,d_r) + 1

    def isBalanced(self, root):
        if not root:
            return True
        res,_ = self.depth(root)
        return res
