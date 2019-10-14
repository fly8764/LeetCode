# Definition for singly-linked list.
'''
方法一：递归法
问题：反转前N个节点
第N+1个节点，successor节点
递归解决，当N=1时，记录successor节点，successor = head.next
和全部反转不同，最后一个节点的next要指向 successor；head.next = successor
问题：反转第m到第n个节点
递归
一直到m= 1，则此时相当于反转前N个节点，
然后把之前的节点拼接起来
这里的递归返回的节点不像 全部反转或反转前N个节点，
这里返回的是正常的节点，相当于才重新拼接一下

方法二：双指针法
in-place
找到第m-1个节点pre，和第m个节点cur
从左往后遍历的过程中，更新 cur.next，pre.next，使得这两个节点反转，
并更新这两个节点，cur.next = temp.next在刚开始更新，pre.next = temp在最后更新

方法三：三指针法
类似于下面的双指针法，只不过这里把tail单独拎出来，并更新，
下面的双指针法，tail每次需要时生成，
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.successor = None

    def reverseBetween1(self, head, m, n):
        # 这种方法没有在开头插入一个哑节点，所以当遇到m = 1时，
        # 没有前面的头指针，即哑节点来拼接后面的反转链表
        if m >= n or not head:
            return head
        start = head
        idx = 1
        while idx < m-1:
            #先不直接到达第m个节点，因为后面要通过next把后面的拼接起来
            head = head.next
            idx += 1

        #找到第n+1个节点，最后把其节点反转好的链表后面
        new = head
        new_idx = idx
        while new_idx <n+1:
            new = new.next
            new_idx += 1

        #为了保存head，后面要通过head.next把反转后的链表接上去
        node = head.next
        idx += 1
        pre_node =None
        p = ListNode(0)
        while idx < n+1:
            idx += 1
            p = ListNode(node.val)
            p.next = pre_node
            pre_node = p
            node = node.next

        head.next = p
        while head.next:
            head = head.next
        head.next = new

        return start

    def reverseBetween2(self, head, m, n):
        if m >= n or not head:
            return head
        start = ListNode(0)
        start.next = head
        p = start
        idx = 0
        while idx < m-1:
            #先不直接到达第m个节点，因为后面要通过next把后面的拼接起来
            p = p.next
            idx += 1

        #找到第n+1个节点，最后把其接在反转好的链表后面
        new = p
        new_idx = idx
        while new_idx <n+1:
            new = new.next
            new_idx += 1

        #为了保存head，后面要通过head.next把反转后的链表接后面
        #node 第m个节点
        node = p.next
        idx += 1
        pre_node =None
        point = ListNode(0)
        while idx < n+1:
            point = ListNode(node.val)
            point.next = pre_node
            pre_node = point
            node = node.next
            idx += 1

        p.next = point
        while p.next:
            p = p.next
        p.next = new

        return start.next

    def reverseBetween3(self, head, m, n):
        #三指针法 哑光节点为m= 1考虑的 in-place 在原链表上改变
        #类似于下面的双指针法，只不过这里把tail单独拎出来，并更新，
        #下面的双指针法，tail每次需要时生成，
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        #找到要反转的起始点的上一个节点，即第m-1个节点
        for _ in range(m-1):
            pre =  pre.next
        #使用三指针pre，start，tail
        #cnt个节点，往前调换cnt-1次即可
        start = pre.next
        tail = start.next #tail紧接在start后面
        for _ in range(n-m):
            start.next = tail.next
            tail.next = pre.next
            pre.next = tail
            tail = start.next
        return dummy.next

    def reverseBetween4(self, head, m, n):
        #双指针法、哑节点 非常好 in-place 相比于三指针法 更简洁一些
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        #pre始终是第m-1个节点
        for _ in range(m-1):
            pre = pre.next

        cur = pre.next
        #这里的循环，cur不改变
        for _ in range(n-m):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp

        return dummy.next

    def reverseList(self, node):
        if not node:
            return node
        if not node.next:
            return node
        last = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return last

    def reverseN(self,head,n):
        if not head:
            return head
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next,n-1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(self, head, m, n):
        # 递归法
        if m == 1:
            return self.reverseN(head,n)
        head.next = self.reverseBetween(head.next,m-1,n-1)
        return head

if __name__ == '__main__':
    so = Solution()
    a = ListNode(3)
    a.next = ListNode(5)
    m= 1
    n = 2
    res = so.reverseBetween(a,m,n)
    while res:
        print(res.val)
        res = res.next