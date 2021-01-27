#coding:gbk
#206
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre
#24
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1

        return dummy.next
#160
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr1, curr2 = headA, headB
        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA

        return curr1
#234
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        slow = head  ##快慢指针
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next         #fast比slow快一半，slow在中间
        slow.next = reverse_list(slow.next)
        slow = slow.next
        while slow:
            if slow.val != head.val:
                return False
            head = head.next
            slow = slow.next
    def reverse_list(self, node):
        pre = None

        while node:
            nex = node.next
            node.next = pre
            pre = node
            node = nex
        return pre

#328  ？？
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenhead = head.next
        odd, even = head, evenhead
        while even and even.next:  #分2条线进行
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head

#19
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next  #[1]  1的情况
        return dummy.next






