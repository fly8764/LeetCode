class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        left, right = [], []
        if root.left:
            left = [str(root.val) + '->' + x for x in self.binaryTreePaths(root.left)]
        if root.right:
            right = [str(root.val)  + '->' + x for x in self.binaryTreePaths(root.right)]
        return left + right

    # def binaryTreePaths(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[str]
    #     """
    #     if not root.left and not root.right:
    #         return [str(root.val)]
    #     left,right = [],[]
    #
    #     if not root.left:
    #         for x in self.binaryTreePaths(root.left):
    #             left += [str(root.val)+ '->'+ str(x)]
    #         for x in self.binaryTreePaths(root.right):
    #             right += [str(root.val) + '->'+str(x)]
    #
    #         # left = [str(root.val) + '->'+str(x) for x in self.binaryTreePaths(root.left)]
    #         # right = [str(root.val) + '->'+str(x) for x in self.binaryTreePaths(root.right)]
    #     return left + right