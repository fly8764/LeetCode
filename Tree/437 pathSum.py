# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 题目说明，路径不一定包含根节点和叶子节点，所有，要遍历所有的可能
# 每个节点都可能 在或者不在路径中
# 单递归：从根节点遍历到每个节点时，从该节点往根节点遍历，必须包含该节点连续
# 路径中，其和满足要求的有多少条
# 双递归，包含该节点和不包含该节点，不包含该节点 又分为 左子树 右子树两种
# 其中用到的递归非常好，从符合要求的节点 返回的过程中，把所有的可能结果累加
class Solution(object):
    def pathSum(self, root, target):
        # 双递归
        if not root:
            return 0

        def dfs(root,target):
            if not root:
                return 0
            cnt = 0
            if root.val == target:
                cnt += 1
            #这种递归循环非常好，从符合要求的节点往上返回，如果只有一种路径，则出栈到最后，结果为1
            #在出栈的过程中，增量来自于 另外一个节点(eg右节点)的可能路径，最后得到所有的路径数
            cnt += dfs(root.left,target - root.val)
            cnt += dfs(root.right,target - root.val)
            return cnt
        # 这种return 就分为必须包含 根节点 和不包含根节点 两类
        return dfs(root,target)+ self.pathSum(root.left,target)+ self.pathSum(root.right,target)


    # def pathSum(self, root, target):
    #     #单递归
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: int
    #     """
    #     self.cnt = 0 #这里为什么非得要加个self
    #     path = []  #这里的path就不要加
    #     def dfs(root):
    #         if not root:
    #             return 0
    #         path.append(root.val)
    #         tmp = 0
    #         #这里要算到根节点，因为 可能出现中间几项和为0
    #         for i in range(len(path)-1,-1,-1):
    #             tmp += path[i]
    #             if tmp == target:
    #                 self.cnt += 1
    #         dfs(root.left)
    #         dfs(root.right)
    #         # 别忘了把加入的这个节点 pop()
    #         path.pop()
    #     dfs(root)
    #
    #     return self.cnt




