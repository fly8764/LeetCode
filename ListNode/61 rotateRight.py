# Definition for singly-linked list.
'''
注意点：
1. 空节点
2.k值的大小，k一般在长度范围内cnt，
如果大于长度范围cnt，要把k对cnt取余，使其在cnt范围内
取余要注意cnt = 1的特殊情况，取余无效，其实这时候就不用再算了，
长度为1的链表，怎么旋转都不会变化
3.cnt = 1，这个一上来要想到，不然后面就可能忘了

方法一：找到链表的长度，把后面k个节点一整串的拼接到开头
方法二：双指针法，也是先找到链表长度，再把后面k个节点使用双指针法 一个一个地
调换到前面
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight1(self, head, k):
        #双指针法
        pass

    def rotateRight(self, head, k):
        if k == 0 or not head:
            return head
        dummy = ListNode(0)
        cnt = 0
        dummy.next = head
        pre = dummy
        while pre.next:
            pre = pre.next
            cnt += 1
        if cnt == 1:
            return head
        #标记尾巴节点
        end = pre
        #k作为除数，要注意k=0的情况，
        # if k > cnt:
        #     temp = k//cnt
        #     k = k - cnt*temp
        # if k == 0:
        #     return head
        # k = 1时，无效
        k %= cnt
        if k == 0:
            return head

        #找到倒数第k+1个节点,next置为空None,执行cnt - k次操作
        node = dummy
        for _ in range(cnt -k):
            node= node.next
        new_start = node.next
        node.next = None

        end.next = dummy.next
        dummy.next = new_start
        return dummy.next


if __name__ == '__main__':
    so = Solution()
    a = ListNode(1)
    start = a
    # for i in range(2,6):
    #     a.next = ListNode(i)
    #     a = a.next
    # while start:
    #     print(start.val)
    #     start = start.next

    res = so.rotateRight(start,k = 12)
    while res:
        print(res.val)
        res = res.next


