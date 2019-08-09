# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root,0)
        return root

    def dfs(self,root,n):
        #temp 是大于 root树的最小值，比如 对于左子树 是其根节点
        if not root:
            return n
        temp = self.dfs(root.right,n) #返回右子树中的最小值，即左子树中最左下角的结点值
        root.val += temp #root节点加上其右子树中的最小值
        temp = self.dfs(root.left,root.val) #将父节点的值加入其左子树中，是大于其左子树的值的最小值
        return temp