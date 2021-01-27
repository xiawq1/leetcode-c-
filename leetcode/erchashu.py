class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left  #####��ڵ�
        self.right = right
######�������Ĳ���

class BinTree():
    def __init__(self):
        self.root = None  #��ʼ�����ڵ�
        self.ls = []   #�����б����ڴ洢�ڵ��ַ
    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            self.ls.append(self.root)
        else:
            rootnode = self.ls[0]  ##����һ��Ԫ����Ϊ���ڵ�
            if rootnode.left == None:
                rootnode.left = node
                self.ls.append(rootnode.left)
            elif rootnode.right == None:
                rootnode.right = node
                self.ls.append(rootnode.right)
                self.ls.pop(0)         #####����self.ls��һ��λ�ô���Ԫ��

#��������ǰ�����
    ##ʹ�õݹ�ķ���ʵ�ֶ�������ǰ�����
    def preorder(self, root):
        if root == None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
# if __name__ == '__main__':
#     tree = BinTree()
#     for i in range(1, 11):
#         tree.add(i)
#     tree.preorder(tree.root)

    #####�������
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    #####�������
    def levelorder(self, root):
        if root == None:
            queue = []
            result = []
            node = root
            queue.append(node)
            while queue:
                node = queue.pop(0)
                result.append(node.data)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            print(result)


#########����һ���������ĸ��ڵ� root �������������������

class Solution {
public:
    void inorder(TreeNode* root, vector<int>& res) {
        if (!root) {
            return;
        }
        inorder(root->left, res);
        res.push_back(root->val);
        inorder(root->right, res);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root, res);
        return res;
    }
};

###########ջ
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)   #######����ڵ����ջ��
                root = root.left
            else:
                leaf = stack.pop()
                res.append(leaf.val)
                root = leaf.right
        return res

'''
����һ������ n������������ 1 ... n Ϊ�ڵ�����ɵ� ����������
'''
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]    #####�ݹ����ֹ����

            allTrees = []
            for i in range(start, end + 1):  # ö�ٿ��и��ڵ�
                # ������п��е�����������
                leftTrees = generateTrees(start, i - 1)   ##########����

                # ������п��е�����������
                rightTrees = generateTrees(i + 1, end)

                # ��������������ѡ��һ������������������������ѡ��һ����������ƴ�ӵ����ڵ���
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []


#����һ������ n������ 1 ... n Ϊ�ڵ���ɵĶ����������ж�����


#####��̬�滮
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

##########��һ�����������ж����Ƿ���һ����Ч�Ķ���������
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val   #######���ڵ��ֵ
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
#������������������дһ�����������������Ƿ���ͬ

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



##����һ�������������㷵���䰴 ������� �õ��Ľڵ�ֵ��
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        level = [root]
        while level:
            current = []
            next_level = []
            for l in level:
                current.append(l.val)
                if l.left:
                    next_level.append(l.left)
                if l.right:
                    next_level.append(l.right)
            ret.append(current)
            level = next_level
        return ret



