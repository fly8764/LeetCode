# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def inorderTraversal(self, root):
    #     res,stack = [],[]
    #     p = root
    #     while p or stack:
    #         while p:
    #             stack.append(p)
    #             p = p.left
    #
    #         temp = stack.pop()
    #         res.append(temp.val)
    #         #开始关注右子树
    #         p = temp.right
    #     return res

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        if root.left:
            res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        if root.right:
            res.extend(self.inorderTraversal(root.right))
        return res

class Solution2:
    def inorder(self,root):
        res,stack = [],[]
        p = root
        while p or stack:
        #这里while循环条件很重要，不仅仅是一个栈，还有节点p
        #使得pop可以写在 while的下面，
        #stack和p同时作为循环结束的条件
            while p:
                #不停的找左子树，依次入栈；出栈时就依次完成遍历
                stack.append(p)
                p = p.left
            node = stack.pop()
            res.append(node.val)
            #开始关注右子树，当节点p访问完后，开始转向右子树
            p = node.right
        return res


