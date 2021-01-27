
#coding:gbk
'''
而满足回溯条件的某个状态的点称为“回溯点”
皇后问题，行列斜
'''
class Solution:
    def solveNQueens(self, n):
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"  ###行列
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row):
            if row == n:   ##回溯出口吗
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)  ###这一列已经被占了
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()  #列
        diagonal1 = set()  #斜线
        diagonal2 = set()  #斜线
        row = ["."] * n  #行
        backtrack(0)
        return solutions
solutions = Solution().solveNQueens(8)
print(len(solutions))
