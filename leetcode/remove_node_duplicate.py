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
            # �����ǰ�ڵ�����һ���ڵ�ֵ��ͬ��ָ������ƶ�
            while head.next and head.val == head.next.val:
                pre = head.val
                head = head.next
            # �����ǰ�ڵ�ֵ��ǰ��ڵ�ֵ������ͬ���򽫵�ǰ�ڵ���ӵ���������
            if head and head.val != pre:
                cur.next = head
                cur = cur.next
            head = head.next
        # ������������ָ�����һ��λ��ָ���
        cur.next = None

        return dummy.next
