
#coding:gbk
'''
���������������ĳ��״̬�ĵ��Ϊ�����ݵ㡱
�ʺ����⣬����б
'''
class Solution:
    def solveNQueens(self, n):
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"  ###����
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row):
            if row == n:   ##���ݳ�����
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)  ###��һ���Ѿ���ռ��
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()  #��
        diagonal1 = set()  #б��
        diagonal2 = set()  #б��
        row = ["."] * n  #��
        backtrack(0)
        return solutions
solutions = Solution().solveNQueens(8)
print(len(solutions))
