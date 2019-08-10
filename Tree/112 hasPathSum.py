# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# **递归**：
# 构造**递归函数**
# 默认情况下，只要没有找到符合要求的叶节点，会一直递归下去，如果到了叶子节点，且满足要求则返回True，否则还会递归下去，但如果为空节点，返回False(没有找到)；
# 如果 满足叶节点 到此时的和为sum，则返回True，
# 通过递归栈，逐层地往上返回True;
#
# **迭代**：
# 栈元素：(node,sum) 当前节点的子树中 需要满去的路径和为sum；
# 没出一个栈元素，获取其当前节点node的子树的要求，node.left sum-node.val，并入栈，
# 当返回True时，就停止了，所以不用遍历所有的情况。
# 当为叶子节点时，其sum 为0，返回True；如果栈空结束时，还没有返回True，则没有找到，返回False。

class Solution:
    def hasPathSum(self, root, sum):
        #迭代,这种方法就不会遍历所有的路径
        #必须到叶子节点才能判断，如果当前的sum大于target，没事，后面可能有负数
        if not root:
            return False
        stack = [(root,sum -root.val),]
        #代表root的子树中的路径目标和为 sum - root.val
        while stack:
            node,temp = stack.pop()
            if not node.left and not node.right and not temp:
                return True
            if node.right:
                stack.append((node.right,temp - node.right.val))
            if node.left:
                stack.append((node.left,temp - node.left.val))
        return False


    # def hasPathSum(self, root, sum):
    #     #简单粗暴的DFS,没有回溯,因此会搜索所有情况，
    #     # 但是 A or B 运算符的特殊情况，当 A True时，就不要计算B了，所以就有了回溯的意思
    #     if not root:
    #         return False
    #     if root.val == sum and not root.left and not root.right:
    #         return True
    #
    #     #遍历所有情况
    #     # left = self.hasPathSum(root.left,sum - root.val)
    #     # right = self.hasPathSum(root.right,sum- root.val)
    #     # return left or right
    #     #这种 A or B 不会遍历所有情况
    #     return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum- root.val)



