#coding:gbk
#200
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        grid[i][j] = '-1'
        orients = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for o in orients:
            p = i + o[0]
            q = j + o[1]
            if p >= 0 and q >= 0 and p < len(grid) and q < len(grid[0]) and grid[p][q] == '1':
                self.dfs(grid, p, q)
        return
Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
#695
class Solution:
    def maxAreaOfIsland(self, grid):

        m = len(grid)
        n = len(grid[0])
        if m == 0:
            return 0
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:

                    area = self.dfs(i, j, grid)
                    res = max(area, res)
        return res
    def dfs(self, m, n, grid):
        area = 1
        grid[m][n] = -1
        orient = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for o in orient:
            p = m + o[0]
            q = n + o[1]
            if p >= 0 and q >= 0 and p < len(grid) and q < len(grid[0]) and grid[p][q] == 1:
                area += self.dfs(p, q, grid)
        return area

#130

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        if len(board) == 0:
            return
        m = len(board)
        n = len(board[0])  #必须在上述判断之后， 否则程序可能会报错，如果当board是个[]的时候
        for i in range(m):
            self.dfs(board, i, 0)
            self.dfs(board, i, n-1)
        for j in range(n):
            self.dfs(board, 0, j)
            self.dfs(board, m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'


    def dfs(self, board, i, j):
        if i >=0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = '-'
            orients = [(-1,0), (1,0), (0,-1),(0,1)]
            for o in orients:
                p = i + o[0]
                q = j + o[1]
                self.dfs(board, p, q)
        return
Solution().solve([["X","X","X","X"],["O","O","O","X"],["X","X","O","X"],["X","O","X","X"]])


#417只需要从四个边界开始遍历即可(类似泛洪的思想, 只要可以从边界出发到达, 就说明该位置的水可以流向对应的海洋)
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # 即找到边界是否能连通到哪些位置即可
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            self.dfs(matrix, i, 0, pacific, matrix[i][0])
            self.dfs(matrix, i, n - 1, atlantic, matrix[i][n - 1])
        for j in range(n):
            self.dfs(matrix, 0, j, pacific, matrix[0][j])
            self.dfs(matrix, m - 1, j, atlantic, matrix[m - 1][j])
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, i, j, visited, pre):
        if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and (not visited[i][j]) and matrix[i][j] >= pre:
            visited[i][j] = True
            self.dfs(matrix, i - 1, j, visited, matrix[i][j])
            self.dfs(matrix, i + 1, j, visited, matrix[i][j])
            self.dfs(matrix, i, j - 1, visited, matrix[i][j])
            self.dfs(matrix, i, j + 1, visited, matrix[i][j])
        return

#529
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if len(board) == 0:
            return []
        m = len(board)
        n = len(board[0])
        # 先实现标记一下哪些点周围有地雷
        orients = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        visited = [[False for _ in range(n)] for _ in range(m)]  # 标记是否访问过
        nums = [[0 for _ in range(n)] for _ in range(m)]  # 标记每个点周围地雷的个数
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'M':
                    for x, y in orients:
                        if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n:
                            nums[i + x][j + y] += 1
        self.dfs(board, click[0], click[1], nums, orients, visited)
        return board

    def dfs(self, board, i, j, nums, orients, visited):
        visited[i][j] = True
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return
        if nums[i][j] > 0:
            board[i][j] = str(nums[i][j])
            return
        if board[i][j] == 'E':
            board[i][j] = 'B'
            for x, y in orients:
                if i + x >= 0 and i + x < len(board) and j + y >= 0 and j + y < len(board[0]) and not visited[i + x][
                    j + y]:
                    self.dfs(board, i + x, j + y, nums, orients, visited)
        return

Solution().updateBoard([['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
, [1,2])

#547
class Solution:
    def findCircleNum(self, isConnected):
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1

        return circles


#257  dfs
class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.right and not root.left:
                    res.append(path)
                    return
                else:
                    path += '->'
                    dfs(root.left, path)
                    dfs(root.right, path)


        if not root:
            return []
        res = []
        dfs(root, '')
        return res

#257 bfs
import collections
class Solution:
    def binaryTreePaths(self, root):
        paths = list()
        if not root:
            return paths

        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])

        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))

                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))
        return paths


#37

class Solution:
    def solveSudoku(self, board):
        def dfs(pos):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return

        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)


Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]
Solution().minDistance("horse", "ros")




