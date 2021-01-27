#coding:gbk

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
def print_by_layer_2(root):
    '''
    3. 终极版
    无line/current_line,在入队时候加入换行标记信息，注意边界条件，防止陷入死循环
    '''
    if not root:
        return
    queue = ["r"] # 一开始塞入一个换行标记，作为队首,任何非TreeNode对象都行。
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if isinstance(node,TreeNode):
            print(node.val, end = " ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            # 边界条件
            if len(queue) > 0:
                queue.append("r") # 对尾添加换行标记
                print()  # 换行
def print_in_one_line(root):
    ''' 1. 简单版： 打印在一行内，不换行 '''
    if not root:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val, end = " ") # end属性默认为“\n”，所以print()函数默认会换行。此处设为空格“ ”，防止自动换行
        if node.left:
            queue.append(node.left) # 将本节点的左子节点入队
        if node.right:
            queue.append(node.right) # 将本节点的右子节点入队
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        stack = [root]
        flag = -1
        while stack:
            lay=[]
            lay_value=[]
            for node in stack:
                lay_value.append(node.val)
                if node.left:
                    lay.append(node.left)
                if node.right:
                    lay.append(node.right)
            stack = lay
            flag += 1
            if flag%2 == 0:

                result.append(lay_value)
            if flag%2 == 1:
                result.append(lay_value[::-1])
        return result


if __name__ == "__main__":
    # 新建节点
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

    # 构建二叉树
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left, node5.right = node10, node11

    # 指定 node1 为root节点
    root = node1

    # 打印
    print("\nprint in one line:")
    print_in_one_line(root)

    print("\n\nprint by layer 1:")
    # print_by_layer_1(root)

    print("\n\nprint by layer 2:")
    print_by_layer_2(root)


