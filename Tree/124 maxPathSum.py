# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#这一题 不想437路径总和，路径必须从上到下，
# 这里的路径可以从左子树到右子树，中间通过父节点
# 对于每个节点，其取值 max(根节点，根节点+左子树，根节点+右子树)
#递归函数每次返回 max(根节点，根节点+左子树路径，根节点+右子树路径)，
#只能返回一条路径，为上面的函数做贡献

class Solution:
    def maxPathSum(self, root):
        self.ret = float('-inf')
        def dfs(root):
            if not root:
                return float('-inf')
            left = dfs(root.left)
            right = dfs(root.right)
            self.ret = max(self.ret,root.val,root.val+left,root.val+right,root.val+right+left)
            return max(left+root.val,right+root.val,root.val)
        dfs(root)
        return self.ret



    # def maxPathSum(self, root):
        #     if not root:
        #         return
        #
        #     self.res = float('-inf')
        #     path = []
        #
        #     def dfs(root):
        #         if not root:
        #             return
        #
        #         path.append(root.val)
        #         temp = 0
        #         for i in range(len(path)-1,-1,-1):
        #             temp += path[i]
        #             self.res = max(self.res,temp)
        #         dfs(root.left)
        #         dfs(root.right)
        #         path.pop()
        #     dfs(root)
        #
        #     return self.res

