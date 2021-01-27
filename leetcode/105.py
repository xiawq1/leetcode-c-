#coding:gbk

class TreeNode():
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
#ǰ�����144
class Solution1():
    def qianxubinali(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)   ###�Ƚ��������������Ҷ���
        return result
def preorderTraversal(now, result=[]):
    if now == None:
        return result
    result.append(now.val)
    preorderTraversal(now.left, result)
    preorderTraversal(now.right, result)
    return result

###�������94
def midorderTraversal(now, result=[]):
    if now == None:
        return result

    midorderTraversal(now.left, result)

    result.append(now.val)
    midorderTraversal(now.right, result)
    return result
#�������
def postorderTraversal(now, result=[]):
    if now == None:
        return
    postorderTraversal(now.left, result)
    postorderTraversal(now.right, result)
    result.append(now.data)
    return result

# if __name__ == "__main__":
# #     # �½��ڵ�
# #     node1 = TreeNode(1)
# #     node2 = TreeNode(2)
# #     node3 = TreeNode(3)
# #     node4 = TreeNode(4)
# #     node5 = TreeNode(5)
# #     node6 = TreeNode(6)
# #     node7 = TreeNode(7)
# #     node8 = TreeNode(8)
# #     node9 = TreeNode(9)
# #     node10 = TreeNode(10)
# #     node11 = TreeNode(11)
# #
# #     # ����������
# #     node1.left, node1.right = node2, node3
# #     node2.left, node2.right = node4, node5
# #     node3.left, node3.right = node6, node7
# #     node4.left, node4.right = node8, node9
# #     node5.left, node5.right = node10, node11
# #
# #     # ָ�� node1 Ϊroot�ڵ�
# #     root = node1
# #     preorderTraversal(root, result=[])
# #     midorderTraversal(root, result=[])

class Solution:
    def buildTree(self, preorder, inorder):
        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            # ǰ������еĵ�һ���ڵ���Ǹ��ڵ�
            preorder_root = preorder_left
            # ����������ж�λ���ڵ�
            inorder_root = index[preorder[preorder_root]]   #####���ڵ��Ӧ������

            # �ȰѸ��ڵ㽨������
            root = TreeNode(preorder[preorder_root])
            # �õ��������еĽڵ���Ŀ
            size_left_subtree = inorder_root - inorder_left
            # �ݹ�ع����������������ӵ����ڵ�
            # ��������С��� ��߽�+1 ��ʼ�� size_left_subtree����Ԫ�ؾͶ�Ӧ����������С��� ��߽� ��ʼ�� ���ڵ㶨λ-1����Ԫ��
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # �ݹ�ع����������������ӵ����ڵ�
            # ��������С��� ��߽�+1+�������ڵ���Ŀ ��ʼ�� �ұ߽硹��Ԫ�ؾͶ�Ӧ����������С��� ���ڵ㶨λ+1 �� �ұ߽硹��Ԫ��
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # �����ϣӳ�䣬�������ǿ��ٶ�λ���ڵ�
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

