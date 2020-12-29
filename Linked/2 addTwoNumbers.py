# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
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

'''
2020/12/13 18:45
按照定义做即可
去个位和十位的值可以使用以下方式：
cur = temp % 10
pre = temp // 10

其实可以将三个写到一个while循环里面，使用or连接即可。
'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return

        p = 0
        dummy = ListNode(-1)
        pre = dummy
        while l1 and l2:
            tmp = l1.val + l2.val + p
            if tmp >= 10:
                node = ListNode(tmp-10)
                p = 1
            else:
                node = ListNode(tmp)
                p = 0
            pre.next = node
            pre = node
            l1 = l1.next
            l2 = l2.next

        while l1:
            tmp = l1.val  + p
            if tmp >= 10:
                node = ListNode(tmp-10)
                p = 1
            else:
                node = ListNode(tmp)
                p = 0
            pre.next = node
            pre = node
            l1 = l1.next

        while l2:
            tmp = l2.val  + p
            if tmp >= 10:
                node = ListNode(tmp-10)
                p = 1
            else:
                node = ListNode(tmp)
                p = 0
            pre.next = node
            pre = node
            l2 = l2.next

        if p:
            node = ListNode(p)
            pre.next = node

        return dummy.next




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



