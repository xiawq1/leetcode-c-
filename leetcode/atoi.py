#coding:gbk

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # ǰ�������һ��ֵΪ���ڵ�
        root = TreeNode(preorder[0])
        # ��Ϊû���ظ�Ԫ�أ����Կ���ֱ�Ӹ���ֵ�����Ҹ��ڵ�����������е�λ��
        mid = inorder.index(preorder[0])
        # ����������
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # ����������
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
if __name__ == '__main__':
    Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])