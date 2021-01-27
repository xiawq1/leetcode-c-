#coding:gbk

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class singlelist():
    def __init__(self, node = None):
        self.__head = node #默认头结点为空
    def empty(self):
        return self.__head is None
    #尾部添加元素
    def append(self, data):
        node = Node(data)
        if self.empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node
    #头部添加元素
    def add(self, data):
        node = Node(data)
        if self.empty():
            self.__head = node
        else:
            node.next = self.__head  ##顺序改变
            self.__head = node   #此时的头结点转变成node
    def length(self):
        if self.empty():
            return 0
        else:
            cur = self.__head
            count = 0
            while cur:
                count += 1
                cur = cur.next
            return count
    def insert(self, pos, data):
        if pos <= 0:
            self.add(data)
        elif pos >= self.length():
            self.append(data)
        else:
            node = Node(data)
            cur = self.__head
            count = 1
            while cur:
                cur = cur.next
                count += 1
                if count == pos:
                    break
            node.next = cur.next
            cur.next = node
    #删除节点
    def remove(self, data):
        if self.empty():
            return False
        cur = self.__head
        pre = None        #定义pre游标，为cur的前一个位置
        while cur:
            if cur.data == data:
                #头结点情况
                if cur == self.__head:
                    self.__head = cur.next  #将头结点赋值给下一个节点
                else:
                    pre.next = cur.next  #删除
            else:
                pre.next = cur   #储存前一个位置
                cur = cur.next
    def search(self, data):
        if self.empty():
            return False
        else:
            cur = self.__head
            while cur:
                if cur.data == data:
                    return True
                else:
                    cur = cur.next
            return False
    #遍历链表
    def travel(self):
        if self.empty():
            return []
        else:
            node_list = []
            cur = self.__head
            while cur:
                node_list.append(cur.data)
                cur = cur.next
        return node_list

###############leetcode练习题

#2

class Solution1():
    def node_sum(self, l1, l2):
        sum = 0
        flag = 0

        res = ListNode(0)
        temp = res
        while l1 and l2:
            if flag == 0:
                res1 = (l1.val + l2.val + sum)//10
                res2 = (l1.val + l2.val + sum) % 10
                sum = res1
                res.val = res2
                flag += 1
            else:
                res1 = (l1.val + l2.val + sum) // 10
                res2 = (l1.val + l2.val + sum) % 10
                sum = res1
                temp.next = ListNode(res2)
                temp = temp.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            res1 = (l1.val + sum) // 10
            res2 = (l1.val + sum) % 10
            sum = res1
            temp.next = ListNode(res2)
            temp = temp.next
            l1 = l1.next
        while l2:
            res1 = (l2.val + sum) // 10
            res2 = (l2.val + sum) % 10
            sum = res1
            temp.next = ListNode(res2)
            temp = temp.next
            l2 = l2.next
        if sum !=0:
            temp.next = ListNode(1)
        return res

#21
class Solution2():
    def merge2list(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1

                l1 = l1.next
            elif l1.val > l2.val:
                temp.next = l2

                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next

#递归解法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
#
# node5 = ListNode(5)
# node6 = ListNode(6)
# node7 = ListNode(7)
# node8 = ListNode(8)
# node5.next = node6
# node6.next = node7
# node7.next = node8
# Solution().mergeTwoLists(node1, node5)

#23
class Solution3():
    def merge_two_list(self, l1, l2):
        temp = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1

                l1 = l1.next
            elif l1.val > l2.val:
                temp.next = l2

                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return temp.next  #这样做node是已经到达最后一个了， 应该像21题，设置一个暂时保存值



    def merge_k_list(self, nodelist):

        for i in range(0, len(nodelist)):
            if i == 0:

                ans = nodelist[0]
            else:
                ans = self.merge_two_list(ans, nodelist[i])
        return ans

#24
class Solution5:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)  #设置哑节点
        dummyHead.next = head    #连接
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next

#25
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):  #翻转
        prev = tail.next
        p = head
        while prev != tail:  #当头和尾相等时，翻转完毕
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)  #哑节点
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next    #如果没有大于k，直接返回
            nex = tail.next #k+1
            head, tail = self.reverse(head, tail)  ##头部，尾部
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next

#61
class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:   ##当节点只有2个时
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head   ##头尾结合

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head

#83

class Solution7():
    def remove_duplicate(self, node):
        if not node:
            return
        if not node.next:  #只有一个节点
            return node

        pre = node  ##暂存地址
        now = pre.next
        now_next = now.next

        while now_next:
            if pre.val == now.val:
                pre.next = now_next
                now = now_next
                now_next = now_next.next
            else:
                pre = now
                now = pre.next
                now_next = now_next.next
            if now.val == pre.val:  #两个节点，且2个节点相同
                pre.next = None
        return node
#82
class Solution8():
    def remove_duplicates2(self, head):
        if not head or not head.next:
            return head
        dummy= pre = ListNode(0)
        dummy.next = head


        while head and head.next:
            if head.val == head.next.val:
                head = head.next

                while head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head.next
            else:
                pre.next = pre.next
            head = head.next
        return dummy.next

##86
class Solution9():
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head
        m = head
        head1 = None
        head2 = None
        while m:
            if m.val < x:
                if head1 is None:
                    head1 = m
                    p = head1  ##p是临时存储地址
                    m = m.next
                else:
                    p.next = m
                    p = m
                    m = m.next
            else:
                if head2 is None:
                    head2 = m
                    q = head2
                    m = m.next
                else:
                    q.next = m
                    q = m
                    m = m.next
        if head1 != None and head2 != None: #注意这里，要分情况讨论
            l = p
            p.next = None
            q.next = None   ###省了这些，运行就会变慢，为什么？，对结果是否有影响
            l.next = head2
            return head1
        if head1 == None and head2:
            return head2
        if head2 == None and head1:
            return head1

##92
class Solution:
    def revr(self, pre, temp):
        nex = temp.next
        p = pre
        while nex != temp:
            nexx = p.next
            p.next = nex
            nex = p
            p = nexx
        return temp, pre


    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        count = 1
        while head:
            tail = pre

            if count == m:
                while count <= n and head.next:
                    tail = tail.next
                    count += 1
                nex = tail.next
                head, tail = self.revr(head, tail)
                pre.next = head
                tail.next = nex
                pre = tail
                head = tail.next




            else:

                head = head.next
                pre = pre.next
            count += 1
        return dummy.next
































