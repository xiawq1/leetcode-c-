#coding:gbk
'''
链表问题
'''

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
#创建节点和连接节点
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

#遍历链表，不可以用head来遍历列表，否则会丢失列表的一些节点 ，可以使用和head相同类型的临时的指针变量

# 先定一个node的类
class Node():  # value + next
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next
    ##获取下一个值
    def getValue(self):
        return self._value
    ##获取下一个节点存的地址
    def getNext(self):
        return self._next
    #设定节点值
    def setValue(self, new_value):
        self._value = new_value
    #设定节点地址
    def setNext(self, new_next):
        self._next = new_next


# 实现Linked List及其各类操作方法
class LinkedList():
    def __init__(self):  # 初始化链表为空表
        self._head = Node()
        self._tail = None
        self._length = 0

    # 检测是否为空
    def isEmpty(self):
        return self._head == None

        # add在链表前端添加元素:O(1)
    ###在前端插入值
    def add(self, value):
        newnode = Node(value, None)  # create一个node（为了插进一个链表）
        newnode.setNext(self._head)   ###设置下一节点的地址
        self._head = newnode   #将该节点设为头结点

    # append在链表尾部添加元素:O(n)
    def append(self, value):
        newnode = Node(value)
        if self.isEmpty():
            self._head = newnode  # 若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()  # 遍历链表
            current.setNext(newnode)  # 此时current为链表最后的元素

    # search检索元素是否在链表中
    def search(self, value):
        current = self._head
        foundvalue = False
        while current != None and not foundvalue:
            if current.getValue() == value:
                foundvalue = True
            else:
                current = current.getNext()
        return foundvalue

    # index索引元素在链表中的位置
    def index(self, value):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError('%s is not in linkedlist' % value)

    # remove删除链表中的某项元素
    def remove(self, value):
        current = self._head
        pre = None
        while current != None:
            if current.getValue() == value:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())  ##前驱节点与下下节点的连接
                break
            else:
                pre = current   ####储存前驱节点
                current = current.getNext()   ##下一节点

    # insert链表中插入元素
    def insert(self, pos, value):
        if pos <= 1:   ###头部
            self.add(value)
        elif pos > self.size():   ##尾部
            self.append(value)
        else:
            temp = Node(value)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current   ##前驱节点
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)

####给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的。
#我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。2
class ListNode:
    def __init__(self, data, next_):
        self.val = data
        self.next = next_
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)   ##########新的加和链表
        resTemp = res   ########创建临时指针变量
        flag = 0
        nextSum = 0
        while l1 != None and l2 != None:
            if flag == 0:
                p = l1.val + l2.val
                res.val = p % 10
                nextSum = int(p / 10)
                flag += 1
            else:
                p = l1.val + l2.val + nextSum
                resTemp.next = ListNode(p%10)
                resTemp = resTemp.next
                nextSum = int(p / 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            p = l1.val + nextSum
            resTemp.next = ListNode(p%10)
            resTemp = resTemp.next
            nextSum = int(p / 10)
            l1 = l1.next
        while l2:
            p = l2.val + nextSum
            resTemp.next = ListNode(p%10)
            resTemp = resTemp.next
            nextSum = int(p / 10)
            l2 = l2.next
        if nextSum != 0:    #######当两条链表结束后，还需要判断是否为0，如果不为0，还需要增加一个值为1 的尾节点
            resTemp.next = ListNode(1)
        return res

############删除链表的倒数第 n 个节点，并且返回链表的头结点 19
###计算链表长度  当遍历到第 L-n+1个节点时，它的下一个节点就是我们需要删除的节点

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:   ##########如果删除的是头结点和尾节点？？
        def getLength(head: ListNode) -> int:
            length = 0
            while head:    #######链表的遍历
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)  ####添加哑节点
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next  #####删除节点，将该节点的前一节点与后一节点连
        return dummy.next   ##返回头结点

#########链表翻转
class Node():
    def __init__(self, data, next_):
        self.value = data
        self.next = next_
    @staticmethod
    def reverse_node(head):
        cur_node = head   ###当前节点
        new_link = None
        while cur_node != None:
            tmp = cur_node.next   ##下一节点
            cur_node.next = new_link
            new_link = cur_node   ###???为什么加这句话
            cur_node = tmp
        return new_link


########给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表25
class Solution:
    # 翻转一个子链表，并且返回新的头与尾， 头与尾翻转
    def reverse(self, head: ListNode, tail: ListNode):   ##？？
        prev = tail.next
        p = head
        while prev != tail:   ##头不等于尾
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)  ###增加虚拟头结点
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            ###找到k个节点的头和尾
            nex = tail.next ###尾的下一个节点
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next

#########################
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def value_to_list(seq):
    head = p = ListNode(float('inf'))
    for su in seq:
        q = ListNode(su)
        p.next = q  #下一节点的位置
        p = q
    return head


def list_to_value(head):
    res = []
    p = head
    while p:
        res.append(str(p.val))
        p = p.next
    return ' '.join(res[1:])

###########双指针
def rotate_k_node_of_list(head, k):
    if k == 1:
        return head
    left = head
    while True:
        front, rear = left.next, left.next
        count = 0
        while rear and count < k:
            rear = rear.next
            count += 1
        if count == k:
            one, two = rotate(front, rear)
            left.next = one
            left = two
        else:
            break
    return head


def rotate(front, rear):
    p, q = front, front
    while q.next and q.next != rear:
        cur = q.next
        q.next = cur.next
        cur.next = p
        p = cur
    return p, q


if __name__ == '__main__':
    seq = list(map(int, input().strip().split()))
    k = int(input().strip())
    head = value_to_list(seq)
    node = rotate_k_node_of_list(head, k)
    res = list_to_value(node)
    print(res)

















#######旋转链表， 将链表每个节点向右移动 k 个位置，其中 k 是非负数。61

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:   ####？？？？
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head
