# Definition for singly-linked list.
'''
大致思路：
把奇偶位置的节点分开，各自串接自己一类的节点，最后在拼接起来
使用双指针，一个是奇数节点，一个是偶数节点
在开头别忘了使用一个临时节点，保存第一个偶数节点，后面把其拼接在奇数尾节点的后面
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        temp = head.next
        #while循环里面的三个条件，有顺序要求
        #首先判断even，其来自于head.next，有可能为空
        #even不为空，则可以判断 even.next
        #odd = head，在开头已经判断了，不为空，可以直接判断odd.next
        while even and even.next and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = temp
        return head
