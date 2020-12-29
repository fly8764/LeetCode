# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def mergeTwoLists(self, l1, l2):
        start = ListNode(0)
        p = start
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                p = p.next
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                p = p.next
                l2 = l2.next
        while l1:
            p.next = ListNode(l1.val)
            p = p.next
            l1 = l1.next
        while l2:
            p.next = ListNode(l2.val)
            p = p.next
            l2 = l2.next
        return start.next


'''
2020/12/12 19:12
第二次做 在起始点做的不好，先进行一次比较选出初始点，然后再进行循环。
可以随便创一个起始点start，最后返回start.next()即可。
'''
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1

        if l1.val > l2.val:
            head = ListNode(l2.val)
            l2 = l2.next
        else:
            head = ListNode(l1.val)
            l1 = l1.next
        pre = head
        while l1 and l2:
            if l1.val > l2.val:
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
            else:
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2

        return pre