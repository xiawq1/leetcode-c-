#coding:gbk
'''
计算二叉树的深度，即算出左子树和右子树的最大深度
max(l,r)+1
'''


#递归的方法
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

#广度优先搜索
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        stack = [root]
        flag = 0
        while stack:
            lay = []

            for node in stack:

                if node.left:
                    lay.append(node.left)
                if node.right:
                    lay.append(node.right)
            stack = lay
            flag += 1

        return flag
