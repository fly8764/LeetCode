# Definition for singly-linked list.
'''
方法一：标记法，每次走过一个节点，做标记，使得其值为float('inf')，下次遇到
标记后的节点时，就说明有环的存在
方法二：快慢指针法，快指针每次走两步，慢指针每次走一步，如果存在环，
两者速度差一，总会相遇；如果不存在环，则不会相遇。
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def hasCycle(self, head):
        # if not head or not head.next:
        #     return False
        fast,slow = head,head
        #while循环条件首先省去了开头的判断是否为空节点或者单个节点的情况
        # 首先判断fast是否为空，然后判断fast.next
        #fast.next使得 fast.next.next可以判断，不出错
        #slow走的慢，上面的两个条件没问题，slow就不会出问题了
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            #这里不能用fast.val == slow.val，因为None节点不存在val
            if fast == slow:
                return True
        return False

    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #使用maxx做标记，一般节点的值不会是maxx
        #但是这种方法修改了链表
        maxx = float('inf')
        # cnt = 0
        while head:
            # cnt += 1
            if head.val == maxx:
                return True
            head.val = maxx
            head = head.next
        return False

'''
2020/12/13 11:35
方法一 标记法

空间复杂度为 o(l)，但是会修改链表


方法二 快慢指针法
快指针每次走两步，慢指针每次走一步，同时出发，在环外不会相遇，一定在环内相遇。
在环内，相当于快指针在追慢指针，慢指针不动，快指针一步一步地追赶。
其中循环条件直接判断fast是否为尾节点即可，毕竟fast走的快，走在前面；然后在循环中判断节点是否相同。
而不是在while 条件中去判断是否相等，while条件判断是否为尾节点。
空间复杂度为 o(l)，同时不会修改链表

第二次没想到快慢指针法，看答案后，对while循环条件一上来没想清楚。
'''
class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False



