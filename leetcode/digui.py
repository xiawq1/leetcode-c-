#coding:gbk

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal(root: TreeNode):
    if root is None:
        return
    # do something here, e.g. print itself
    print(root.val)

    preorderTraversal(root.left)
    preorderTraversal(root.right)

def preorderTraversal(root: TreeNode):
    stack=[(root,False)]
    while len(stack)>0:
        tree,extend=stack.pop()
        if tree is None:
            continue
        if not extend:
            stack.append((tree.right,False))
            stack.append((tree.left,False))
            stack.append((tree,True))
        else:
            # do something here, e.g. print itself
            print(tree.val)
def inorderTraversal(root: TreeNode):
    if root is None:
        return
    inorderTraversal(root.left)
    # do something here, e.g. print itself
    print(root.val)
    inorderTraversal(root.right)
def inorderTraversal(root: TreeNode):
    stack=[(root,False)]
    while len(stack)>0:
        tree,extend=stack.pop()
        if tree is None:
            continue
        if not extend:
            stack.append((tree.right,False))
            stack.append((tree,True))
            stack.append((tree.left,False))
        else:
            # do something here, e.g. print itself
            print(tree.val)
#�Ӻͺ���
def listsum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + listsum(nums[1:])
    '''
    �ݹ��㷨�����н�����������С��ģ�����ֱ�ӽ����
    �����ܸı������ģ����С�����ģ��
    �����������
    '''

#����һ�����
def recMC(coin, change):
    mincoin = change
    if change in coin:
        knownres[change] = 1    #��¼���Ž�
        return 1
    elif knownres[change] > 0:
        return knownres[change]
    else:
        for i in [c for c in coin if c<=change]:
            numcoins = 1 + recMC(coin, change-i, knownres)
            if numcoins < mincoin:
                mincoin = numcoins
                knownres[change] = mincoin
        return mincoin

recMC([1,5,10,25], 63, [0]*64)


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