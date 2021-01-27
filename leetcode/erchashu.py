class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left  #####左节点
        self.right = right
######二叉树的插入

class BinTree():
    def __init__(self):
        self.root = None  #初始化根节点
        self.ls = []   #定义列表用于存储节点地址
    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            self.ls.append(self.root)
        else:
            rootnode = self.ls[0]  ##将第一个元素设为根节点
            if rootnode.left == None:
                rootnode.left = node
                self.ls.append(rootnode.left)
            elif rootnode.right == None:
                rootnode.right = node
                self.ls.append(rootnode.right)
                self.ls.pop(0)         #####弹出self.ls第一个位置处的元素

#二叉树的前序遍历
    ##使用递归的方法实现二叉树的前序遍历
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

    #####中序遍历
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    #####层序遍历
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


#########给定一个二叉树的根节点 root ，返回它的中序遍历。

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

###########栈
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
                stack.append(root)   #######将左节点加入栈内
                root = root.left
            else:
                leaf = stack.pop()
                res.append(leaf.val)
                root = leaf.right
        return res

'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树
'''
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]    #####递归的终止条件

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)   ##########？？

                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []


#给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种


#####动态规划
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

##########定一个二叉树，判断其是否是一个有效的二叉搜索树
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val   #######根节点的值
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
#给定两个二叉树，编写一个函数来检验它们是否相同

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



##给你一个二叉树，请你返回其按 层序遍历 得到的节点值。
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



