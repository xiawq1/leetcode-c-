#coding:gbk
'''
���������ǿգ����������ϵ����нڵ�Ĺؼ���ֵ��С�ڸ��ڵ�Ĺؼ���ֵ
���������ǿգ����������ϵ����нڵ�Ĺؼ���ֵ�����ڸ��ڵ�Ĺؼ���ֵ
'''
class TreeNode():
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.val)

#���ڶ���������ǵݹ鶨��ģ�����ڵ�Ĺ����ǣ���ԭ���������Ϊ�գ���ֱ�Ӳ��룻�������ؼ��� k С�ڸ��ڵ�ؼ��֣�����뵽�������У����ؼ��� k ���ڸ��ڵ�ؼ��֣�����뵽�������С�

class BST():
    def __init__(self, node=None):
        '''
        ���ø��ڵ�
        :param node: ���ڵ�
        '''
        node = TreeNode(node)
        self.root_node = node

    def insert(self, x):
        '''
        ���������������
        :param x:
        :return:
        '''
        if self.is_exist(x):#�ж������Ƿ���ڸýڵ�
            return
        p = TreeNode(x)
        if self.root_node == None:#�����Ϊ�յĻ����򽫲���Ľڵ���Ϊ���ڵ�
            self.root_node = p
        else:
            cur = self.root_node
            pre = None
            while cur != None:#���÷ǵݹ�ķ�������
                pre = cur
                if cur.val < x:
                    cur = cur.right
                else:
                    cur = cur.left

            p.parent = pre
            if pre.val < x:
                pre.right = p
            else:
                pre.left = p

    def is_exist(self, k):
        '''
        �ж϶��������Ƿ����ĳ�ڵ����ֵ�� k ���
        :param k:
        :return:
        '''
        cur = self.root_node
        while cur != None and cur.val != k:
            if k < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return True if cur != None else False

    def find_node(self, k):
        '''
        �ҵ�ֵΪk�Ľڵ㲢����
        :param k:
        :return:
        '''
        cur = self.root_node
        while cur != None and cur.val != k:
            if k < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return cur

if __name__ == '__main__':
    bs_tree = BST(16)   #��ʼ��������
    #�Զ��������������
    bs_tree.insert(9)
    bs_tree.insert(24)
    bs_tree.insert(12)
    bs_tree.insert(6)
    bs_tree.insert(20)
    bs_tree.insert(30)