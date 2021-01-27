#coding:gbk
'''
�����㷨���ܽ�
���
result = []
def backtrack('·��', 'ѡ���б�'):
    if �����������:
        result.add('·��')
        return
    for ѡ�� in ѡ���б�:
        ��ѡ��
        backtrack('·��', 'ѡ���б�')
        ����ѡ��
'''

#46  ȫ��������  ����һ��û���ظ����ֵ����У����������п��ܵ�����
class Solution:
    def permute(self, nums):
        if not nums:
            return nums

        ##��¼·��
        res = []
        def backtrack(nums, temp):
            ###��������
            if not nums:
                res.append(temp[:])
            n = len(nums)
            for i in range(n):
                temp.append(nums[i])
                backtrack(nums[:i]+nums[i+1:], temp)  ##nums[:i]+nums[i+1:]����ȥnums[i]
                ###ȡ��ѡ��
                temp.pop()

        backtrack(nums, [])
        return res

########22��������

class Solution:
    def generateParenthesis(self, n):

        res = []

        def backstrack(temp, left, right):
            # ��������
            if len(temp) == 2 * n:
                res.append("".join(temp))
                return
            # ��ʼ���б���
            # ���õ�������left�����õ�������right
            if left < n:
                # ��ѡ��
                temp.append('(')
                # ��һ�־���
                backstrack(temp, left + 1, right)
                # ����
                temp.pop()
            # ͬ��
            if right < left:
                temp.append(')')
                backstrack(temp, left, right + 1)
                temp.pop()

        backstrack([], 0, 0)
        return res

#####�������

class Solution:
    def combinationArray(self, candidates, target):

        candidates.sort()
        res = []  # �����Ͻ��
        size = len(candidates)

        def backtrack(combination, cur_sum, j):
            # combinationĿǰ�Ѿ����������,cur_sum��ǰ����ͣ�j���ڿ�����͵Ĳ��ҷ�Χ���
            # �ݹ����
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(combination)
            for i in range(j, size):  # j�����ظ�
                if cur_sum + candidates[i] > target:  # Լ������(��)
                    break
                j = i
                backtrack(combination + [candidates[i]], cur_sum + candidates[i], j)  # �ݹ����

        backtrack([], 0, 0)
        return res
######38 �ַ���������,��ӡ�����ַ����������ַ�������
class Solution:
    def permutation(self, s):
        if not s: return
        strs=list(sorted(s)) #sorted�Կɵ�������Կ��Բ��������ҷ����µĶ���
        res=[]
        def backtrack(strs,tmp):
            if not strs: res.append(''.join(tmp))
            for i in range(len(strs)):
            #ȥ��
                if i>0 and strs[i]==strs[i-1]:  #�����ظ�Ԫ��
                    continue
             #������һ�������
                backtrack(strs[:i]+strs[i+1:],tmp+[strs[i]])
        backtrack(strs,[])
        return res


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
                    diagonal1.add(row - i)  ###�Խ���
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)  ###��������
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
# solutions = Solution().solveNQueens(8)
# print(len(solutions))


##��������
class solution():
    def get_token_way(self, n):
        ways = []
        def backTrack(s, left, right):
            if len(s) == 2*n:
                ways.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backTrack(s, left+1, right)
                s.pop()########������ʱɾ�����һ��
            if right < left:
                s.append(')')
                backTrack(s, left, right+1)
                s.pop()
        backTrack([], 0, 0)
        return ways
# ways = solution().get_token_way(4)

#46.����һ�� û���ظ� ���ֵ����У����������п��ܵ�ȫ���С�
class Solution():
    def permute(self, nums):
        permutions = []

        def backTrack(nums, temp):
            if not nums:
                permutions.append(temp[:])
            n = len(nums)
            for i in range(n):

                temp.append(nums[i])
                backTrack(nums[:i]+nums[i+1:], temp)
                temp.pop()
        backTrack(nums, [])
        return permutions

#######����һ���ɰ����ظ����ֵ����� nums ��������˳�� �������в��ظ���ȫ���С�47
#���ݼӼ�֦

class solution1():
    def permute2(self, nums):
        permutions = []
        size = len(nums)
        nums.sort()  ##����

        def backTrack(nums, temp):
            if len(temp) == size:
                permutions.append(temp[:])
            n = len(nums)
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1]:   ###��֦
                    continue
                temp.append(nums[i])
                backTrack(nums[:i] + nums[i + 1:], temp)
                temp.pop()

        backTrack(nums, [])
        return permutions
#����һ�����ظ�Ԫ�ص����� candidates ��һ��Ŀ���� target ���ҳ� candidates �����п���ʹ���ֺ�Ϊ target ����ϡ�



class Solution(object):
    def combinationSum(self, candidates, target):

        length = len(candidates)   ####�б���

        res = []

        def dfs(target, index, maybe):
            if target < 0:
                return
            if target == 0:
                res.append(maybe)
                return
            for i in range(index, length):
                dfs(target - candidates[i], i, maybe + [candidates[i]])

        dfs(target, 0, [])
        return res
#����һ������ candidates ��һ��Ŀ���� target ���ҳ� candidates �����п���ʹ���ֺ�Ϊ target ����ϡ����ݼӼ�֦

from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:  ###�ظ�
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


res = Solution().combinationSum2([10,1,2,7,6,1,5], 8)
print(res)


#�����ظ�Ԫ�ص��������� nums�����ظ��������п��ܵ��Ӽ�  78
class Solution():
    def get_ziji(self, nums):
        result = []
        size = len(nums)
        if size == 0:
            return result
        def backtrack(path, start):
            result.append(path)
            if start == size: ####
                return
            for i in range(start, size):
                backtrack(path+[nums[i]], i+1)
        backtrack([], 0)
        return result

#####����һ�����ܰ����ظ�Ԫ�ص��������� nums�����ظ��������п��ܵ��Ӽ�90
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)
        if size == 0:
            result.append([])
            return

        nums.sort()

        def backtrack(path, start):
            result.append(path)  # ÿһƬҶ�Ӷ�����Ҫ�Ĵ�
            if start == size:
                return
            for i in range(start, size):
                if i > start and nums[i - 1] == nums[i]:  # ��֤ͬ�㲻�ظ�����������ͬ
                    continue
                backtrack(path + [nums[i]], i + 1)

        backtrack([], 0)
        return result
#46
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return nums
        result = []
        def backtrack(path, nums):
            if not nums:
                result.append(path[:])
                return
            n = len(nums)
            for i in range(n):
                path.append(nums[i])
                backtrack(path, nums[:i] + nums[i+1:])
                path.pop()

        backtrack([], nums)
        return result
#47
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        nums.sort()
        def backtrack(path, nums):
            if not nums:
                result.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(path + [nums[i]], nums[:i] + nums[i+1:])
        backtrack([], nums)
        return result

#39
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        result = []
        def backtrack(res, path, start):
            if res == 0:
                result.append(path)
                return
            if res < 0:        ####ȱ���������һֱ����
                return

            for i in range(start, len(candidates)):

                backtrack(res-candidates[i], path+[candidates[i]], i)

        backtrack(target, [], 0)
        return result

#40
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()
        n = len(candidates)
        if n == 0:
            return []
        def backtrack(res, path, start):
            if target == 0:
                result.append(path)
                return
            if target < 0 or start >= n:
                return

            for i in range(start, n):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                backtrack(res-candidates[i], path+[candidates[i]], i+1)
        backtrack(target, [], 0)
        return result

#78
class Solution:
    def subsets(self, nums):
        n = len(nums)
        if n == 0:
            return []
        result = []

        def backtrack(start, path):
            result.append(path)
            if start == n:

                return
            for i in range(start, n):
                backtrack(i+1, path+[nums[i]])
        backtrack(0, [])
        return result

#90


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        result = []
        nums.sort()
        def backtrack(path, start):
            result.append(path)
            if start == n:
                return
            for i in range(start, n):
                if i > start and nums[i-1] == nums[i]:
                    continue
                backtrack(path+[nums[i]], i+1)
        backtrack([], 0)
        return result
Solution().subsetsWithDup([1,2,2])

#79
class Solution(object):
    def exist(self, board, word):
        row = len(board)   #hang
        col = len(board[0])  #lie
        if row == 0:
            return False
        mark = [[0 for _ in range(col)] for _ in range(row)]
        def backtrack(i, j, mark, word):
            if len(word) == 0:
                return True
            if not (i >= 0 and j >= 0 and i < row and j < col):
                return False
            if mark[i][j] == 1:   ##�߹��Ĳ������ߵ���˼��
                return False
            if board[i][j] == word[0]:
                mark[i][j] = 1
                #�����з���ֵҪ�ȸ�ֵ��
                fanhuiz = backtrack(i+1, j, mark, word[1:]) or backtrack(i-1, j, mark, word[1:]) or backtrack(i, j-1, mark, word[1:]) or backtrack(i, j+1, mark, word[1:])
                #�������ֱ��if not (backtrack(i+1, j, mark, word[1:]) or backtrack(i-1, j, mark, word[1:]) or backtrack(i, j-1, mark, word[1:]) or backtrack(i, j+1, mark, word[1:]))
                if not fanhuiz:
                    mark[i][j] = 0 #���ݣ���Ϊ�����û����ȥ�����������൱��û��
                    return False
                else:
                    return True
            return False
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, mark, word):
                    return True
        return False


Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "FCE")

#22
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        result = []
        def backtrack(path, left, right):
            if right > left:
                return
            if len(path) == 2*n:
                result.append(path)
                return
            if left < n:
                backtrack(path+'(', left+1, right)
            if right < n:
                backtrack(path+')', right+1)
        backtrack('', 0, 0)
        return result

#51
class Solution:
    def solveNQueens(self, n):
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()  #��
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n  #��
        backtrack(0)
        return solutions

solutions = Solution().solveNQueens(4)