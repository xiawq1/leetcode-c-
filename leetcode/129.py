#coding:gbk
'''
����һ��������������ÿ����㶼���һ�� 0-9 �����֣�ÿ���Ӹ���Ҷ�ӽڵ��·��������һ�����֡�
'''


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        total = 0
        nodeQueue = collections.deque([root])
        numQueue = collections.deque([root.val])

        while nodeQueue:
            node = nodeQueue.popleft()
            num = numQueue.popleft()
            left, right = node.left, node.right
            if not left and not right:
                total += num
            else:
                if left:
                    nodeQueue.append(left)
                    numQueue.append(num * 10 + left.val)
                if right:
                    nodeQueue.append(right)
                    numQueue.append(num * 10 + right.val)

        return total
