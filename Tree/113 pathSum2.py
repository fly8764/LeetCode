# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #在DFS遍历的过程中，记录沿线的各个节点值，到达符合要求的叶子节点后，把路径 保存到结果中；
    # 而不是一路地递归，找到符号要求的叶子节点后，再依次出栈的记录沿线经过的节点

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        #全局变量，记录遍历过程中符合要求的结果
        res = []
        def dfs(root,temp_sum,cur):
            if not root:
                return
            #下面换用新的变量，若使用 cur += [root.val] 递归会对其产生影响
            new_sum =temp_sum- root.val
            new_cur =cur+ [root.val]
            if not new_sum and not root.left and not root.right:
                res.append(new_cur)
                return #别忘了返回，不然还会往下递归
            dfs(root.left,new_sum,new_cur)
            dfs(root.right,new_sum,new_cur)
        dfs(root, sum, [])
        return res