#coding:gbk
'''
��������
'''

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
#�����ڵ�����ӽڵ�
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

#����������������head�������б�����ᶪʧ�б��һЩ�ڵ� ������ʹ�ú�head��ͬ���͵���ʱ��ָ�����

# �ȶ�һ��node����
class Node():  # value + next
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next
    ##��ȡ��һ��ֵ
    def getValue(self):
        return self._value
    ##��ȡ��һ���ڵ��ĵ�ַ
    def getNext(self):
        return self._next
    #�趨�ڵ�ֵ
    def setValue(self, new_value):
        self._value = new_value
    #�趨�ڵ��ַ
    def setNext(self, new_next):
        self._next = new_next


# ʵ��Linked List��������������
class LinkedList():
    def __init__(self):  # ��ʼ������Ϊ�ձ�
        self._head = Node()
        self._tail = None
        self._length = 0

    # ����Ƿ�Ϊ��
    def isEmpty(self):
        return self._head == None

        # add������ǰ�����Ԫ��:O(1)
    ###��ǰ�˲���ֵ
    def add(self, value):
        newnode = Node(value, None)  # createһ��node��Ϊ�˲��һ������
        newnode.setNext(self._head)   ###������һ�ڵ�ĵ�ַ
        self._head = newnode   #���ýڵ���Ϊͷ���

    # append������β�����Ԫ��:O(n)
    def append(self, value):
        newnode = Node(value)
        if self.isEmpty():
            self._head = newnode  # ��Ϊ�ձ�����ӵ�Ԫ����Ϊ��һ��Ԫ��
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()  # ��������
            current.setNext(newnode)  # ��ʱcurrentΪ��������Ԫ��

    # search����Ԫ���Ƿ���������
    def search(self, value):
        current = self._head
        foundvalue = False
        while current != None and not foundvalue:
            if current.getValue() == value:
                foundvalue = True
            else:
                current = current.getNext()
        return foundvalue

    # index����Ԫ���������е�λ��
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

    # removeɾ�������е�ĳ��Ԫ��
    def remove(self, value):
        current = self._head
        pre = None
        while current != None:
            if current.getValue() == value:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())  ##ǰ���ڵ������½ڵ������
                break
            else:
                pre = current   ####����ǰ���ڵ�
                current = current.getNext()   ##��һ�ڵ�

    # insert�����в���Ԫ��
    def insert(self, pos, value):
        if pos <= 1:   ###ͷ��
            self.add(value)
        elif pos > self.size():   ##β��
            self.append(value)
        else:
            temp = Node(value)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current   ##ǰ���ڵ�
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)

####�������� �ǿ� ������������ʾ�����Ǹ������������У����Ǹ��Ե�λ���ǰ��� ���� �ķ�ʽ�洢�ġ�
#���ǽ��������������������᷵��һ���µ���������ʾ���ǵĺ͡�2
class ListNode:
    def __init__(self, data, next_):
        self.val = data
        self.next = next_
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)   ##########�µļӺ�����
        resTemp = res   ########������ʱָ�����
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
        if nextSum != 0:    #######��������������󣬻���Ҫ�ж��Ƿ�Ϊ0�������Ϊ0������Ҫ����һ��ֵΪ1 ��β�ڵ�
            resTemp.next = ListNode(1)
        return res

############ɾ������ĵ����� n ���ڵ㣬���ҷ��������ͷ��� 19
###����������  ���������� L-n+1���ڵ�ʱ��������һ���ڵ����������Ҫɾ���Ľڵ�

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:   ##########���ɾ������ͷ����β�ڵ㣿��
        def getLength(head: ListNode) -> int:
            length = 0
            while head:    #######����ı���
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)  ####����ƽڵ�
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next  #####ɾ���ڵ㣬���ýڵ��ǰһ�ڵ����һ�ڵ���
        return dummy.next   ##����ͷ���

#########����ת
class Node():
    def __init__(self, data, next_):
        self.value = data
        self.next = next_
    @staticmethod
    def reverse_node(head):
        cur_node = head   ###��ǰ�ڵ�
        new_link = None
        while cur_node != None:
            tmp = cur_node.next   ##��һ�ڵ�
            cur_node.next = new_link
            new_link = cur_node   ###???Ϊʲô����仰
            cur_node = tmp
        return new_link


########����һ������ÿ k ���ڵ�һ����з�ת�����㷵�ط�ת�������25
class Solution:
    # ��תһ�����������ҷ����µ�ͷ��β�� ͷ��β��ת
    def reverse(self, head: ListNode, tail: ListNode):   ##����
        prev = tail.next
        p = head
        while prev != tail:   ##ͷ������β
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)  ###��������ͷ���
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # �鿴ʣ�ಿ�ֳ����Ƿ���ڵ��� k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            ###�ҵ�k���ڵ��ͷ��β
            nex = tail.next ###β����һ���ڵ�
            head, tail = self.reverse(head, tail)
            # �����������½ӻ�ԭ����
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
        p.next = q  #��һ�ڵ��λ��
        p = q
    return head


def list_to_value(head):
    res = []
    p = head
    while p:
        res.append(str(p.val))
        p = p.next
    return ' '.join(res[1:])

###########˫ָ��
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

















#######��ת���� ������ÿ���ڵ������ƶ� k ��λ�ã����� k �ǷǸ�����61

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
        while old_tail.next:   ####��������
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
