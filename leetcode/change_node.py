
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None


class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        # add a new node pointed to previous node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val)

ListNode_1 = ListNode_handle()
l1 = ListNode()
l1_list = [1,8,3]
for i in l1_list:
    l1 = ListNode_1.add(i)
print(l1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
