# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def reverseList(self, node):
    #     # 递归
    #     # not node是为空节点准备的
    #     # node.next要预先判断，否则node.next.next不存在，会出错
    #     if not node or not node.next:
    #         return node
    #     # 返回 反转后的新的起点
    #     start = self.reverseList(node.next)
    #     # 这里把node接在其下一个节点的后面，同时把自己与下一个节点的连续断掉
    #     # node.next = None
    #     node.next.next = node
    #     node.next = None
    #     return start

    def reverseList(self, node):
        #迭代
        if not node:
            return node
        p = node
        pre = None
        while node:
            p = ListNode(node.val)
            p.next = pre
            pre = p
            node = node.next
        return p
