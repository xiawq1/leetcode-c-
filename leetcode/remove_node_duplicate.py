# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummy = ListNode(0)
        cur = dummy
        pre = None
        while head:
            # 如果当前节点与下一个节点值相同，指针向后移动
            while head.next and head.val == head.next.val:
                pre = head.val
                head = head.next
            # 如果当前节点值与前后节点值均不相同，则将当前节点添加到新链表中
            if head and head.val != pre:
                cur.next = head
                cur = cur.next
            head = head.next
        # 最后将新链表最后指针的下一个位置指向空
        cur.next = None

        return dummy.next
