# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers1(self, l1, l2):
        #新建一个链表
        pre = 0
        # 作为头指针，不存第一个有效值,从node.next开始存值
        node = ListNode(0)
        p = node
        while l1 and l2:
            temp = l1.val + l2.val + pre
            cur = temp % 10
            pre = temp // 10
            p.next = ListNode(cur)
            p = p.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            temp = l1.val + pre
            cur = temp % 10
            pre = temp // 10
            p.next = ListNode(cur)
            p = p.next
            l1 = l1.next

        while l2:
            temp = l2.val + pre
            cur = temp % 10
            pre = temp // 10
            p.next = ListNode(cur)
            p = p.next
            l2 = l2.next

        if pre:
            p.next = ListNode(pre)

        return node.next

    def addTwoNumbers(self, l1, l2):
        #在原始链表上修改,空间复杂度并没有改变，时间稍微快一点
        pre = 0
        # start = ListNode(0)
        # start.next = l1
        start = l1
        pre_l1 = l1
        while l1 and l2:
            temp = l1.val + l2.val + pre
            cur = temp %10
            pre = temp //10
            l1.val = cur
            pre_l1 = l1
            l1 = l1.next
            l2 = l2.next

        while l1:
            temp = l1.val + pre
            cur = temp %10
            pre = temp //10
            l1.val = cur
            pre_l1 = l1
            l1 = l1.next

        while l2:
            temp = l2.val + pre
            cur = temp %10
            pre = temp // 10
            # l1 = ListNode(cur)
            pre_l1.next = ListNode(cur)
            pre_l1 = pre_l1.next
            l2 = l2.next

        if pre:
            pre_l1.next = ListNode(pre)
        # return start.next
        return start


if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(5)
    res = Solution().addTwoNumbers(l1,l2)
    while res:
        print(res.val)
        res = res.next

    l1 = ListNode(0)
    l2 = ListNode(7)
    l2.next = ListNode(3)
    res = Solution().addTwoNumbers(l1,l2)
    while res:
        print(res.val)
        res = res.next



