# Definition for singly-linked list.
'''
方法一：递归法
建立在已经解决好的子问题上
先 last = self.reverseList(node.next)
使得第二个节点（包括）以后的链表反转好，返回最后的头节点last
然后 node.next.next = node  node.next = None
反转第一、第二个节点之间的关系
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    # def reverseList(self, node):
    #     # 递归
    #     # not node是为空节点准备的
    #     # node.next要预先判断，否则node.next.next不存在，会出错
    #     if not node or not node.next:
    #         return node
    #     # 返回 反转后的新的起点
    #     start = self.reverseList(node.next)
    #     # 这里把node接在其下一个节点的后面，同时把自己与下一个节点的连续断掉
    #     # node.next = None
    #     node.next.next = node
    #     node.next = None
    #     return start

    def reverseList1(self, node):
        #迭代
        if not node:
            return node
        p = node
        pre = None
        while node:
            p = ListNode(node.val)
            p.next = pre
            pre = p
            node = node.next
        return p

    def reverseList(self, node):
        if not node:
            return node
        if not node.next:
            return node
        last = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return last

'''
2020/12/12 18:40

方法一 递归
关键找到递归逻辑，递归终止条件。
这题需要返回头节点，即反转链表后的头节点，所以每次递归要返回头节点，这个头节点从递归的最底层
一直递归到开始，中间不变，因此比较特殊。
递归逻辑：每次都假设递归已经处理好底层链表；然后处理当前节点和递归函数入口节点之间的关系，即反转。
每次递归函数返回的起始节点返回出去。
终止条件：node.next == None的节点none即为最后一个节点，找到这个节点，即可返回。
第二次做也没想起来。

方法二 迭代法
head代表已经反转的链表的尾节点，每次迭代不需要更新（注意），因为其用来连接已反转和未反转链表。
每次需要把尾节点的next连接到已反转链表的头节点，因此每次迭代时需要把已反转链表的头节点记录下来，如tmp = dummy.next

注：2020/12/25 下午两点面试百度时，做的这个题目，当时结果是 4->3
缺少了第14行和写错第19行：使得每次迭代时，把已经反转的链表扔掉了，
多于了第20行：使得每次迭代时，待反转的链表和已经反转的链表没有联系；
while head and head.next:
    tmp = dummy.next
    dummy.next = head.next
    head.next = head.next.next
    dummy.next.next = tmp
    # head = head.next
'''

class Solution2:
    def reverseList1(self, head):
        if not head:
            return

        node = ListNode(head.val)
        head = head.next
        while head:
            tmp = ListNode(head.val)
            tmp.next = node
            node = tmp
            head = head.next

        return node

    def reverseList(self, head):
        if not head:
            return
        if not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


class Solution:
    # 迭代法
    def reverse(self,head):
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head
        while head and head.next:
            tmp = dummy.next
            dummy.next = head.next
            head.next = head.next.next
            dummy.next.next = tmp

        return dummy.next



if __name__  == '__main__':
    so = Solution()
    dummy = ListNode(-1)
    head = ListNode(1)
    dummy.next = head
    for i in range(2,6):
        print(head.val)
        head.next = ListNode(i)
        head = head.next
    print(head.val)

    print('-'*10)

    res = so.reverse(dummy.next)

    while res:
        print(res.val)
        res = res.next





