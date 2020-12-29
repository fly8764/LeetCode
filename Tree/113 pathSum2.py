# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
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

'''
2020/12/11 0:40
stack中的元素(node,tmp)表示将node加入到路径后，其还差的元素值。

'''
class Solution2:
    # 网站后台报错
    def pathSum(self, root, sum):
        if not root:
            return []

        stack = [(root,0,[])]
        res = []
        while stack:
            node,tmp,cur = stack.pop()
            if not node.left and not node.right and tmp + node.val == sum:
                res.append(cur+[node])

            if node.left:
                stack.append((node.left,tmp + node.val,cur+[node]))
            if node.right:
                stack.append((node.right,tmp + node.val,cur+[node]))

        return res

    # stack中的元素(node,tmp_sum,tmp_path)表示当前路径的判断节点为node，其路径tmp_path还不包含node，临时和tmp_sum也不包含node
    # 需要在下一步判断。
    def pathSum2(self, root, sum):
        if not root:
            return []

        stack = [(root,0,[]),]
        res = []
        while stack:
            node,tmp_sum,cur = stack.pop()
            if not node.left and not node.right and tmp_sum + node.val == sum:
                res.append(cur+[node.val])

            if node.left:
                stack.append((node.left,tmp_sum + node.val,cur+[node.val]))
            if node.right:
                stack.append((node.right,tmp_sum + node.val,cur+[node.val]))

        return res


class Solution:
    # 回溯法
    def pathSum(self, root, sum):
        res = []
        if not root:
            return []

        def dfs(root,sum,path):
            if not root:
                return

            # tmp_sum = sum - root.val
            # tmp_path = path + [root.val]
            if not root.left and not root.right and sum - root.val == 0:
                res.append(path + [root.val])
                return

            dfs(root.left, sum - root.val, path + [root.val])
            dfs(root.right, sum - root.val, path + [root.val])

        dfs(root,sum,[])
        return res

