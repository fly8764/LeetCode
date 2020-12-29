# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#这种方法 是 从底往上 递归
#DFS(后序遍历) + 回溯法(现在认为回溯法就是 DFS在递归时 剪枝，返回)，本体是回溯 mid
#当left,right,mid有两个为True时，结果就可以一定是 root.val
#每次递归返回 当前有没有找到p or q，返回给上层 递归看
#注意 题目中给的p，q是树节点，而不是值

#测试
class Solution1:
    def lowestCommonAncestor(self, root, p, q):
        self.res = None
        self.dfs(root,p,q)
        return self.res

    def dfs(self,root,p,q):
        if not root:
            return 0

        left = self.dfs(root.left,p,q)
        right = self.dfs(root.right,p,q)
        mid = root == p or root == q
        if left + right + mid > 1:
            self.res = root
        return left or right or mid

'''
2020/12/10 20:00
DFS（后续遍历）
常规的递归题目，清楚
递归逻辑、递归函数的参数及返回结果、终止条件。
p，q的存在情况有三种，分别在节点root的左右子树中；都在左子树或右子树中。
分别在左右子树，则节点root就是结果，直接返回；都集中在一边，则返回对应的子树根节点。

'''
class Solution:
    def lowestCommonAncestor1(self, root, p, q):
        self.res = None
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            mid = root.val == p.val or root.val == q.val
            if left + right + mid > 1:
                self.res = root

            return left or right or mid

        dfs(root)
        return self.res

    def lowestCommonAncestor(self, root, p, q):
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        elif not left and right:
            return right
        else:
            return left