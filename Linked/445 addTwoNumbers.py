# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        pre_node = None
        p = ListNode(0)
        pre = 0
        while stack1 and stack2:
            temp = stack1.pop() + stack2.pop() + pre
            cur = temp %10
            pre = temp //10
            p = ListNode(cur)
            p.next = pre_node
            pre_node = p

        while stack1:
            temp = stack1.pop() + pre
            cur = temp %10
            pre = temp//10
            p = ListNode(cur)
            p.next = pre_node
            pre_node = p

        while stack2:
            temp = stack2.pop() + pre
            cur = temp %10
            pre = temp //10
            p = ListNode(cur)
            p.next = pre_node
            pre_node = p
        if pre:
            p = ListNode(pre)
            p.next = pre_node
        return p


'''
2020/12/13 19:08
逆序处理 栈
'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack1.append(l2.val)
            l2 = l2.next

        pre = None
        carry = 0
        while stack1 or stack2 or carry > 0:
            a = 0 if not stack1 else stack1.pop()
            b = 0 if not stack2 else stack2.pop()
            cur = a + b + carry
            # tmp = cur%10
            # carry = cur//10
            carry = cur // 10
            cur %= 10
            node = ListNode(cur)
            node.next = pre
            pre = node
        return pre

