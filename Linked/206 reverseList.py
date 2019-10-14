# Definition for singly-linked list.
'''
方法一：递归法
建立在已经解决好的子问题上
先 last = self.reverseList(node.next)
使得第二个节点（包括）以后的链表反转好，返回最后的头节点last
然后 node.next.next = node  node.next = None
反转第一、第二个节点之间的关系
'''
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

    def reverseList1(self, node):
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

    def reverseList(self, node):
        if not node:
            return node
        if not node.next:
            return node
        last = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return last

