# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        #双指针法，不适用额外的内存
        fast,slow = head, head
        while True:
            #注意这里如果不存在环，python 返回空即可
            if not fast or not fast.next:
                return
                #或 return  None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        idx = 0
        while head:
            if head not in dic:
                dic[head] = idx
                idx += 1
                head = head.next
            else:
                return head
        return None


    def detectCycle2(self, head):
        #使用集合，速度更快一些，集合可以去除重复元素
        #但是节点即使同值也不是同一个节点，内存地址也必须相同，
        #使用了额外内存
        dic = set()
        p = head
        idx = 0
        while p:
            if p not in dic:
                dic.add(p)
                idx += 1
                p = p.next
            else:
                return p
        return None

