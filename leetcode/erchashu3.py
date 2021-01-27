#coding:gbk
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        flag = 0
        while stack:
            temp = []
            for res in stack:

                if res.left:
                    temp.append(res.left)
                if res.right:
                    temp.append(res.right)
            stack = temp
            flag += 1
        return flag
