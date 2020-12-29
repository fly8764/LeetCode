# Definition for a binary tree node.
'''
中序遍历的来递归
方法一：
二叉搜索树 的**中序遍历**的结果是一个**递增序列**
因此，可以将其中序遍历结果 排个序，观察是否和排序前相等，相等该数就是二叉搜索树。
二叉搜索树数，是**严格大于，小于**，因此，需要用将排序结果 转化成**集合set()**，排除相等元素
方法二：
常规的根据定义递归
方法三：
极致递归，一种更新维护，last值，中序遍历过程中的最大值，当根节点的值大于last时，
更新last=root.val，然后继续递归右子树；若last> = root.val，
则不符合定义，返回False。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    #     def isValidBST(self, root: TreeNode) -> bool:
    #         result =  self.dfs(root)
    #         if sorted(list(set(result))) ==result:#使用set()排除相等项 左子树小于(不是小于等于)根节点
    #         # if sorted(result) ==result:
    #             # print(result)
    #             return True
    #         else:
    #             # print(result)
    #             return False

    #     def dfs(self,root):
    #         res = []
    #         if  not root :
    #             return []
    #         res += self.dfs(root.left)
    #         res.append(root.val)
    #         res += self.dfs(root.right)
    #         return res

    def dfs(self,root):
        if not root.left and not root.right:
            return True, root.val, root.val

        left,right,mid = False,False,False
        # left_max,left_min = 0,0
        if root.left:
            left,left_min,left_max = self.dfs(root.left)
        else:
            left = True
            left_min,left_max  = root.val,root.val -1

        # right_max,right_min = 0,0
        if root.right:
            right,right_min,right_max = self.dfs(root.right)
        else:
            right = True
            right_min, right_max = root.val+1,root.val

        if root.val > left_max and root.val < right_min:
            mid = True
        return (left and right and mid),left_min,right_max

    def isValidBST(self, root):
        if not root:
            return True
        res,_,_ = self.dfs(root)
        return res

        # if not root:
        #     return False
        #
        # if not root.left and not root.right:
        #     return True, root.val, root.val
        #
        # left, right, mid = False, False, False
        # left_max, left_min = 0, 0
        # if root.left:
        #     left, left_min, left_max = self.isValidBST(root.left)
        # right_max, right_min = 0, 0
        # if root.right:
        #     right, right_min, right_max = self.isValidBST(root.right)
        #
        # if root.val > left_max and root.val < right_min:
        #     mid = True
        # return (left and right and mid), left_min, right_max
'''
2020/12/8 1:38
第二次没做出来

方法一 中序遍历
利用二叉搜索树的性质：中序遍历是一个严格的递增数列

方法二 递归
搞清楚递归的模板和流程，然后注意其中的细节
每次递归需要返回该节点为根节点的BST的有效结果、该树的最大值（在其右子树上或root）、该树的最小值（在其左子树上或root）
注意在节点为空时，如何设置其最大最小值
'''
class Solution:
    # 利用二叉搜索树的性质：中序遍历是一个严格的递增数列
    def isValidBST1(self, root):
        res = []
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            node = stack.pop()
            res.append(node.val)
            p = node.right
        res_new = list(set(res))
        res_new.sort()

        return res == res_new

    def dfs(self,root):
        if not root.left and not root.right:
            return True,root.val,root.val

        # 返回左子树的有效情况、最大值、最小值
        # 当左子树不存在时，因为要返回左子树的最小值，此时为root.val;
        # 对该根节点进行比较判断左子树的最大值时，left_max一定要小于root.val，
        # 所以赋值为root.val - 1
        if root.left:
            left,left_min,left_max = self.dfs(root.left)
        else:
            left = True
            left_max,left_min = root.val  - 1, root.val

        # 返回右子树的有效情况、最大值、最小值
        # 当右子树不存在时，因为要返回右子树的最大值，此时为root.val;
        # 对该根节点进行比较判断右子树的最小值时，right_min一定要大于root.val，
        # 所以赋值为root.val + 1
        if root.right:
            right, right_min, right_max = self.dfs(root.right)
        else:
            right = True
            right_max,right_min = root.val,root.val + 1

        mid = False
        if root.val > left_max and root.val < right_min:
            mid = True

        return (left and right and mid), left_min, right_max


    def isValidBST(self, root):
        if not root:return True
        res,_,_ = self.dfs(root)
        return res


