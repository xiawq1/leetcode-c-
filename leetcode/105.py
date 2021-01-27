#coding:gbk

class TreeNode():
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
#前序遍历144
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
                stack.append(node.left)   ###先进后出，所以左子叶后进
        return result
def preorderTraversal(now, result=[]):
    if now == None:
        return result
    result.append(now.val)
    preorderTraversal(now.left, result)
    preorderTraversal(now.right, result)
    return result

###中序遍历94
def midorderTraversal(now, result=[]):
    if now == None:
        return result

    midorderTraversal(now.left, result)

    result.append(now.val)
    midorderTraversal(now.right, result)
    return result
#后序遍历
def postorderTraversal(now, result=[]):
    if now == None:
        return
    postorderTraversal(now.left, result)
    postorderTraversal(now.right, result)
    result.append(now.data)
    return result

# if __name__ == "__main__":
# #     # 新建节点
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
# #     # 构建二叉树
# #     node1.left, node1.right = node2, node3
# #     node2.left, node2.right = node4, node5
# #     node3.left, node3.right = node6, node7
# #     node4.left, node4.right = node8, node9
# #     node5.left, node5.right = node10, node11
# #
# #     # 指定 node1 为root节点
# #     root = node1
# #     preorderTraversal(root, result=[])
# #     midorderTraversal(root, result=[])

class Solution:
    def buildTree(self, preorder, inorder):
        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]   #####根节点对应的索引

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

