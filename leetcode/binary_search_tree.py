#coding:gbk
'''
若左子树非空，则左子树上的所有节点的关键字值均小于根节点的关键字值
若右子树非空，则右子树上的所有节点的关键字值均大于根节点的关键字值
'''
class TreeNode():
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.val)

#由于二叉查找树是递归定义的，插入节点的过程是：若原二叉查找树为空，则直接插入；否则，若关键字 k 小于根节点关键字，则插入到左子树中，若关键字 k 大于根节点关键字，则插入到右子树中。

class BST():
    def __init__(self, node=None):
        '''
        设置根节点
        :param node: 根节点
        '''
        node = TreeNode(node)
        self.root_node = node

    def insert(self, x):
        '''
        二叉树做插入操作
        :param x:
        :return:
        '''
        if self.is_exist(x):#判断树中是否存在该节点
            return
        p = TreeNode(x)
        if self.root_node == None:#如果树为空的话，则将插入的节点置为根节点
            self.root_node = p
        else:
            cur = self.root_node
            pre = None
            while cur != None:#利用非递归的方法遍历
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
        判断二叉树中是否存在某节点的数值与 k 相等
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
        找到值为k的节点并返回
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
    bs_tree = BST(16)   #初始化二叉树
    #对二叉树做插入操作
    bs_tree.insert(9)
    bs_tree.insert(24)
    bs_tree.insert(12)
    bs_tree.insert(6)
    bs_tree.insert(20)
    bs_tree.insert(30)