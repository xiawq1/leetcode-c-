
#coding:gbk

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root):
        def maxGain(node):
            if not node:
                return 0

            # �ݹ���������ӽڵ�������ֵ
            # ֻ���������ֵ���� 0 ʱ���Ż�ѡȡ��Ӧ�ӽڵ�
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # �ڵ�����·����ȡ���ڸýڵ��ֵ��ýڵ�������ӽڵ�������ֵ
            priceNewpath = node.val + leftGain + rightGain

            # ���´�
            self.maxSum = max(self.maxSum, priceNewpath)

            # ���ؽڵ�������ֵ
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
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
    Solution().maxPathSum(root)