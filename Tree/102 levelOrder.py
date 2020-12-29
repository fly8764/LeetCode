# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        parent = [root]

        while parent:
            child = []
            cur = []
            for _ in range(len(parent)):
                node = parent.pop(0)
                cur.append(node.val)
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)

            res.append(cur)
            parent = child[:]

        return res
'''
2020/12/6 0:46
第二次做，内层循环使用了while queue，和外层循环一样的条件，感觉会有问题；
看到第一次做的答案，可以用for循环，使用len()来处理。
'''
class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            tmp_queue = []
            tmp_res = []
            for _ in range(len(queue)):
                q = queue.pop(0)
                tmp_res.append(q.val)
                if q.left:
                    tmp_queue.append(q.left)
                if q.right:
                    tmp_queue.append(q.right)
            queue = tmp_queue[:]
            res.append(tmp_res)

        return res






