#coding:gbk
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # ��ʼ������ͬʱ����һ��ڵ��������У������ڵ�
        Q = collections.deque([root])              #�Ƚ��ȳ���duilie

        # ���� while ѭ���������ǲ���
        while Q:

            # ��¼��ǰ���д�С
            size = len(Q)

            # ������һ������нڵ�
            for i in range(size):

                # �Ӷ���ȡ��Ԫ��
                node = Q.popleft()

                # ����
                if i < size - 1:
                    node.next = Q[0]

                # ��չ��һ��ڵ�
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # ���ظ��ڵ�
        return root


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

#117
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root

        def BFS(oneLayer):
            nextLayer = []  # ÿһ�ζ�����յ��б�ȥ����nextLayer
            for i in oneLayer:
                if i.left:
                    nextLayer.append(i.left)
                if i.right:
                    nextLayer.append(i.right)

            if len(nextLayer) > 1:  # һ��ֻ��1���ڵ��û��Ҫ���ˡ�
                for j in range(0, len(nextLayer) - 1):
                    nextLayer[j].next = nextLayer[j + 1]  # ÿ���ڵ��nextָ�����һ���ڵ㡣

            if nextLayer:  # nextLayer���ǿյĻ��ͼ��������ߡ�
                BFS(nextLayer)

        BFS([root])  # �ʼ����ֻ��һ��һ�����ڵ㡣
        return root


class Solution {
public:
    Node* connect(Node* root) {
        if (!root) {
            return nullptr;
        }
        queue<Node*> q;
        q.push(root);
        while (!q.empty()) {
            int n = q.size();
            Node *last = nullptr;
            for (int i = 1; i <= n; ++i) {
                Node *f = q.front();
                q.pop();
                if (f->left) {
                    q.push(f->left);
                }
                if (f->right) {
                    q.push(f->right);
                }
                if (i != 1) {
                    last->next = f;
                }
                last = f;
            }
        }
        return root;
    }
};
