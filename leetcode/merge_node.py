

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # �ϲ��� l1 �� l2 ���ֻ��һ����δ���ϲ��꣬����ֱ�ӽ�����ĩβָ��δ�ϲ����������
        prev.next = l1 if l1 is not None else l2

        return prehead.next
