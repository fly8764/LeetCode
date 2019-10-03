# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self,root):
        res,stack = [],[]
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res

    def dfs(self,root):
        if not root:
            return
        self.dfs(root.left)
        self.nums.append(root.val)
        self.dfs(root.right)

    def findTarget(self, root, target):
        self.nums = []
        nums = self.inorder(root)
        size = len(nums)
        left,right = 0,size-1
        while left < right:
            temp = nums[left] + nums[right]
            if temp == target:
                return True
            elif temp < target:
                left += 1
            else:
                right -= 1

        return False