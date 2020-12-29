# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution3:
    def preorder(self, root):
        res = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res
    # def preorder(self, root):
    #     if not root:
    #         return []
    #
    #     res = [root.val]
    #     children = root.children
    #     if  children:
    #         for child in children:
    #             res += self.preorder(child)
    #     return res

class Solution2:
    def preorder(self,root):
        if not root:return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res

    def preorder2(self,root):
        res = []
        stack = [root] if root else []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack.extend(node.children[::-1])
            # if node.right:
            #     stack.append(node.right)
            # if node.left:
            #     stack.append(node.left)
        return res


class Solution4:
    '''
    这里写的方法有两层循环，外侧主要靠stack，内层靠p，自然的思路。
    上面的解法，上来就把p放到stack中，每次新的左节点也放进去，同时把右节点也放进去，
    不过是倒过来放，这样pop()时，先出左节点，等往左走完了，再依次出右节点。不过这种
    方法需要有children属性。
    '''
    def preorderTraversal(self,root):
        if not root:return []
        result,stack = [],[]
        p = root
        # 一直不停的往左走
        while p or stack:
            while p:
                result.append(p.val)
                if p.right:
                    stack.append(p.right)
                p = p.left
            if stack:
                p = stack.pop()

        return result


class Solution:
    def preorder(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.children:
                stack.extend(p.children[::-1])
        return res


