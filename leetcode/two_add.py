# coding=gbk

class ListNode(object):
    def __init__(self, x):
        self.val = x  #########存放数值
        self.next = None  #######存放下一节点的位置
class LinkList:
    def __init__(self):
        self.head = None
    def initList(self, data):
        self.head = ListNode(data[0])

        r = self.head
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next  #返回的是p的话，是节点的的最后一个
        return r
    def printlist(self, head):
        if head == None:return
        node = head
        while node != None:
            print(node.val, end = ' ')
            node = node.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = head
        q = head.next
        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next
        return p
class Solution2:
    def addtwo(self, l1:ListNode, l2:ListNode)->ListNode:
        head = point = ListNode(0)
        carry = 0
        while l1 or l2:
            new_point = ListNode(0)
            if not l1:
                sum = l2.val + carry
                new_point.val = sum % 10
                carry = sum // 10
                l2 = l2.next
            elif not l2:
                sum = l1.val + carry
                new_point.val = sum % 10
                carry = sum // 10
                l1 = l1.next
            else:
                sum = (l1.val + l2.val + carry)
                new_point.val = sum % 10
                carry = sum // 10
                l1 = l1.next
                l2 = l2.next
            point.next = new_point
            point = point.next
            print(point)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def dfs(l, r, i):
            if not l and not r and not i: return None
            s = (l.val if l else 0) + (r.val if r else 0) + i
            node = ListNode(s % 10)
            node.next = dfs(l.next if l else None, r.next if r else None, s // 10)
            return node
        return dfs(l1, l2, 0)




if __name__ == '__main__':
    a = Solution2()
    l=LinkList()
    data1 = [1, 2, 3]
    data2 = [2, 4, 6]
    l1=l.initList(data1)

    l2=l.initList(data2)
    l.printlist(l1)
    # print("\r")
    # l.printlist(l2)
    # print("\r")
    # m=a.mergeTwoLists(l1,l2)
    # l.printlist(m)
    a.addtwo(l1, l2)



