# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS(后序遍历) + 回溯
#这题是 二叉搜索树，可以利用其性质，只在根节点的一个子树上递归，即剪枝
class Solution1:
    def lowestCommonAncestor(self, root, p, q):
        #迭代法, 比递归法 少了一些出栈，递归中当找到公共节点时，其实可以不用
        #停止递归，出栈，但是还需要出栈，
        if p.val > q.val:
            p,q = q,p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                return root



    # def lowestCommonAncestor(self, root, p, q):
    #     self.res = None
    #     def dfs(root,p,q):
    #         if not root:
    #             return 0
    #
    #         left,right = 0,0
    #         if root.val >p.val and root.val > q.val:
    #             left = dfs(root.left,p,q)
    #         elif root.val < p.val and root.val < q.val :
    #             right = dfs(root.right, p, q)
    #         else:
    #             left = dfs(root.left,p,q)
    #             right = dfs(root.right,p,q)
    #         mid = root == p or root == q
    #
    #         if left + right + mid > 1:
    #             self.res = root
    #         return left or right or mid
    #     dfs(root,p,q)
    #     return self.res

    # def lowestCommonAncestor(self, root, p, q):
    #     self.res = None
    #
    #     def dfs(root,p,q):
    #         if not root:
    #             return 0
    #         left = dfs(root.left,p,q)
    #         right = dfs(root.right,p,q)
    #         mid = root == p or root == q
    #         if mid + left + right > 1:
    #             self.res = root
    #         return left or right or mid
    #
    #     dfs(root,p,q)
    #     return self.res


'''
2020/12/10 19:56
方法一 递归
前提条件 二叉搜索树，说明是个有序的树，可以利用其性质，根据根节点和目标节点值的大小关系，选择递归方向（剪枝）。
遇到目标节点，如何处理？遇到一个或者两个分布如何应对？
当前节点和左右子树的寻找结果分布用变量表示，公共节点即同时找到，此时需要三个结果之和来指示。
这种返回遍历结果的方法不是很容易想到。
可以使用常规的递归函数做。

方法二 迭代
二叉搜索树是有序的，可以利用这个条件。
最近祖先节点root和目标节点p,q的值有三种情况，
若root < p,q，则向右子树寻找；若root > p,q，则左子树寻找；
若 p < root < q，则root满足要求。
这个逻辑也用在递归函数中。

'''
class Solution:
    # 递归
    def lowestCommonAncestor1(self, root, p, q):
        self.res = None
        def dfs(node,p,q):
            if not node:
                return 0
            left,right = 0,0
            if node.val > p.val and node.val > q.val:
                left = dfs(node.left,p,q)
            elif node.val < p.val and node.val < q.val:
                right = dfs(node.right,p,q)
            else:
                left = dfs(node.left, p, q)
                right = dfs(node.right, p, q)
            mid = root.val == p.val or root.val == q.val

            if left + right + mid > 1:
                self.res = root
            return left or right or mid
        dfs(root,p,q)
        return self.res

    # 递归2
    def lowestCommonAncestor(self, root, p, q):
        if root.val == p.val or root.val == q.val or not root:
            return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor2(root.right,p,q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        else:
            return root

    # 迭代
    def lowestCommonAncestor2(self, root, p, q):
        if p.val > q.val:
            p,q = q,p

        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root

