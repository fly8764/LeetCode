# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
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

'''
2020/12/13 12:30
方法 快慢双指针法
需要分析快慢指针第一次相遇时，两者走的步数，
第一次相遇时两ru者的步数 fast = s+nb,slow = s其中b为环的节点数，fast比slow都绕了n圈。
另一方面 fast = 2slow 即 s + nb = 2s,所以s = nb。
假设头节点到入口的节点数为a，则到达入口的步数为 a+nb，对比快慢指针第一次相遇时慢指针的步数slow = nb
发现，slow再走a步就行了，因此可以再设一个指针，让其在两者相遇后从头节点出发，再走a步，
此时其和slow同时到达入口节点。

'''
class Solution:
    def detectCycle(self, head):
        fast,slow = head,head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast



