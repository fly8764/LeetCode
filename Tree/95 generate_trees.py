# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #对应这种要找到所有可能的解的题目，一般都是用递归来做，
    #所有的解，通过递归遍历所有的情况
    def generateTrees(self, n):
        if n == 0:
            return []
        def generate(start,end):
            #这个if段，是最底层的情况
            if start > end:
                return [None,] #逗号 加不加都行
            all_trees = []

            for i in range(start,end+1):
                left_tree = generate(start,i-1)
                right_tree = generate(i+1,end)

                for l in left_tree:
                    for r in right_tree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            return all_trees
        return generate(1,n)


