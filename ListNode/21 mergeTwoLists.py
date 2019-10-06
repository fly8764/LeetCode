# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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