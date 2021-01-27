#coding:gbk

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
def print_by_layer_2(root):
    '''
    3. �ռ���
    ��line/current_line,�����ʱ����뻻�б����Ϣ��ע��߽���������ֹ������ѭ��
    '''
    if not root:
        return
    queue = ["r"] # һ��ʼ����һ�����б�ǣ���Ϊ����,�κη�TreeNode�����С�
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if isinstance(node,TreeNode):
            print(node.val, end = " ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            # �߽�����
            if len(queue) > 0:
                queue.append("r") # ��β��ӻ��б��
                print()  # ����
def print_in_one_line(root):
    ''' 1. �򵥰棺 ��ӡ��һ���ڣ������� '''
    if not root:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val, end = " ") # end����Ĭ��Ϊ��\n��������print()����Ĭ�ϻỻ�С��˴���Ϊ�ո� ������ֹ�Զ�����
        if node.left:
            queue.append(node.left) # �����ڵ�����ӽڵ����
        if node.right:
            queue.append(node.right) # �����ڵ�����ӽڵ����
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        stack = [root]
        flag = -1
        while stack:
            lay=[]
            lay_value=[]
            for node in stack:
                lay_value.append(node.val)
                if node.left:
                    lay.append(node.left)
                if node.right:
                    lay.append(node.right)
            stack = lay
            flag += 1
            if flag%2 == 0:

                result.append(lay_value)
            if flag%2 == 1:
                result.append(lay_value[::-1])
        return result


if __name__ == "__main__":
    # �½��ڵ�
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)

    # ����������
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left, node5.right = node10, node11

    # ָ�� node1 Ϊroot�ڵ�
    root = node1

    # ��ӡ
    print("\nprint in one line:")
    print_in_one_line(root)

    print("\n\nprint by layer 1:")
    # print_by_layer_1(root)

    print("\n\nprint by layer 2:")
    print_by_layer_2(root)


