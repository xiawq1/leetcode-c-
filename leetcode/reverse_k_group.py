class Solution:
    # ��תһ�����������ҷ����µ�ͷ��β
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # �鿴ʣ�ಿ�ֳ����Ƿ���ڵ��� k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # �����������½ӻ�ԭ����
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next
