#coding:gbk

#144

#ǰ�����    ջ
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left

            else:
                leaf = stack.pop()
                root = leaf.right
        return res
#�ݹ�

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = []
        preorder(root)
        return res
#�������

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                leaf = stack.pop()
                res.append(leaf.val)
                root = leaf.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        res = []
        inorder(root)
        return res

#�������

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()
        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

#�������

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            lay = []
            lay_result = []
            for node in queue:
                lay_result.append(node.val)
                if node.left:
                    lay.append(node.left)
                if node.right:
                    lay.append(node.right)
            queue = lay
            res.append(lay_result)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []  # ��Ŷ�������α����Ľ��
        if root is None:
            return levels

        def help(root, level):
            if len(levels) == level:  # ��������
                levels.append([])
            levels[level].append(root.val)
            if root.left:  # ѭ������
                help(root.left, level + 1)
            if root.right:
                help(root.right, level + 1)

        help(root, 0)
        return levels

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        flag = 1
        while queue:
            lay = []
            lay_result = []
            flag += 1

            for node in queue:
                lay_result.append(node.val)
                if node.right:
                    lay.append(node.right)
                if node.left:
                    lay.append(node.left)

            queue = lay
            if flag % 2 == 0:

                res.append(lay_result[::-1])
            if flag % 2 == 1:
                res.append(lay_result)
        return res

#96
#һ���ǽ�ÿ���ڵ㵱�ɸ��ڵ����һ��
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

#95
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]

            allTrees = []
            for i in range(start, end + 1):  # ö�ٿ��и��ڵ�
                # ������п��е�����������
                leftTrees = generateTrees(start, i - 1)

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

#98
'''
����һ�����������ж����Ƿ���һ����Ч�Ķ�����������

����һ��������������������������

�ڵ��������ֻ����С�ڵ�ǰ�ڵ������
�ڵ��������ֻ�������ڵ�ǰ�ڵ������
�������������������������Ҳ�Ƕ���������

'''

#����������ڵ�ֻ�����һ��Խ��ԽС���ҽڵ�ֻ�ܱ���һ��Խ��Խ��Ŷԡ�  �ݹ�
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if node is None:
                return True
            value = node.val
            if value <= lower or value >= upper:
                return False
            if not helper(node.left, lower, value):
                return False
            if not helper(node.right, value, upper):
                return False
            return True

        return helper(root)
#����������������ֱ���������12345�����ڵ�ǰһ�������Ⱥ�һ����ҪС����ˣ�1.���ȵõ�����������2.�ж��Ƿ�ǰһ�����Ⱥ�һ����С�� �������

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left

            else:
                leaf = stack.pop()
                res.append(leaf.val)
                root = leaf.right
        for i in range(len(res)-1):
            if res[i] > res[i+1]:
                return False
                break
        return True
#100
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        queue = deque([p, q], )
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True





#101

from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        def check(p, q): #����ݹ��ж������Ƿ����
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        queue = deque([(root, root), ])
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.right))
                queue.append((p.right, q.left))
        return True

#104     ���ڵ㵽��ԶҶ�ӽڵ���·���ϵĽڵ�����������

#105  �ҵ����������ĸ��ڵ� root
# �����ø��ڵ��������
# �����ø��ڵ��������



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

#106

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:len(postorder)-1])
        return root

#108
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        root_index = len(nums) // 2
        root = TreeNode(nums[root_index])
        root.left = self.sortedArrayToBST(nums[:root_index])
        root.right = self.sortedArrayToBST(nums[root_index+1:])
        return root

#110
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def helper(node, level):
            if node is None:
                return level
            left_tree = helper(node.left, level+1)
            right_tree = helper(node.right, level+1)
            if abs(left_tree - right_tree) > 1:
                self.res = False
            return max(left_tree, right_tree)
        helper(root, 0)
        return self.res

#111

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def help(node, level):
            if node is None:
                return level
            if not node.left:
                return help(node.right, level+1)
            if not node.right:
                return help(node.left, level+1)
            return min(help(node.left, level+1), help(node.right, level+1))
        return help(root, 0)


#112
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        sum = sum - root.val
        if not root.left and not root.right and sum == 0:    #���ڵ㵽Ҷ�ӽڵ���ڵ�·��
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)   ##�����߻���������

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        que_node = deque([root])
        que_val = deque([root.val])
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False

#113
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        def helper(root, tmp, sum_):
            if not root:
                return
            if not root.left and not root.right and sum_ - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
            helper(root.left, tmp + [root.val], sum_ - root.val)
            helper(root.right, tmp + [root.val], sum_ - root.val)
        res = []
        helper(root, [], sum_)
        return res
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root: return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if not node.right and not node.left and sum(tmp) == sum_:
                res.append(tmp)
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
        return res


#437

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def helper(self, node, curr):
        if not node:
            return
        if node.val == curr:
            # print('satisfy node:',node.val)
            self.ans += 1
            # return
        # print('dfs node val:',node.val,'curr val:',curr,'sum:',sum)
        self.helper(node.left, curr - node.val)
        self.helper(node.right, curr - node.val)

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.helper(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)

        return self.ans






