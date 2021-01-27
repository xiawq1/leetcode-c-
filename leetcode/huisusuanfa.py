#coding:gbk
'''
回溯算法的总结
框架
result = []
def backtrack('路径', '选择列表'):
    if 满足结束条件:
        result.add('路径')
        return
    for 选择 in 选择列表:
        做选择
        backtrack('路径', '选择列表')
        撤销选择
'''

#46  全排列问题  给定一个没有重复数字的序列，返回其所有可能的序列
class Solution:
    def permute(self, nums):
        if not nums:
            return nums

        ##记录路径
        res = []
        def backtrack(nums, temp):
            ###触发条件
            if not nums:
                res.append(temp[:])
            n = len(nums)
            for i in range(n):
                temp.append(nums[i])
                backtrack(nums[:i]+nums[i+1:], temp)  ##nums[:i]+nums[i+1:]，除去nums[i]
                ###取消选择
                temp.pop()

        backtrack(nums, [])
        return res

########22括号生成

class Solution:
    def generateParenthesis(self, n):

        res = []

        def backstrack(temp, left, right):
            # 结束条件
            if len(temp) == 2 * n:
                res.append("".join(temp))
                return
            # 开始进行遍历
            # 可用的左括号left，可用的右括号right
            if left < n:
                # 做选择
                temp.append('(')
                # 下一轮决策
                backstrack(temp, left + 1, right)
                # 撤回
                temp.pop()
            # 同理
            if right < left:
                temp.append(')')
                backstrack(temp, left, right + 1)
                temp.pop()

        backstrack([], 0, 0)
        return res

#####数字组合

class Solution:
    def combinationArray(self, candidates, target):

        candidates.sort()
        res = []  # 存放组合结果
        size = len(candidates)

        def backtrack(combination, cur_sum, j):
            # combination目前已经产生的组合,cur_sum当前计算和，j用于控制求和的查找范围起点
            # 递归出口
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(combination)
            for i in range(j, size):  # j避免重复
                if cur_sum + candidates[i] > target:  # 约束函数(剪)
                    break
                j = i
                backtrack(combination + [candidates[i]], cur_sum + candidates[i], j)  # 递归回溯

        backtrack([], 0, 0)
        return res
######38 字符串的排列,打印出该字符串中所有字符的排列
class Solution:
    def permutation(self, s):
        if not s: return
        strs=list(sorted(s)) #sorted对可迭代对象皆可以操作，并且返回新的对象
        res=[]
        def backtrack(strs,tmp):
            if not strs: res.append(''.join(tmp))
            for i in range(len(strs)):
            #去重
                if i>0 and strs[i]==strs[i-1]:  #避免重复元素
                    continue
             #进行下一层决策树
                backtrack(strs[:i]+strs[i+1:],tmp+[strs[i]])
        backtrack(strs,[])
        return res


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
                    diagonal1.add(row - i)  ###对角线
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)  ###撤销操作
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
# solutions = Solution().solveNQueens(8)
# print(len(solutions))


##回溯条件
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
                s.pop()########不满足时删掉最后一个
            if right < left:
                s.append(')')
                backTrack(s, left, right+1)
                s.pop()
        backTrack([], 0, 0)
        return ways
# ways = solution().get_token_way(4)

#46.给定一个 没有重复 数字的序列，返回其所有可能的全排列。
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

#######给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。47
#回溯加剪枝

class solution1():
    def permute2(self, nums):
        permutions = []
        size = len(nums)
        nums.sort()  ##排序

        def backTrack(nums, temp):
            if len(temp) == size:
                permutions.append(temp[:])
            n = len(nums)
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1]:   ###剪枝
                    continue
                temp.append(nums[i])
                backTrack(nums[:i] + nums[i + 1:], temp)
                temp.pop()

        backTrack(nums, [])
        return permutions
#给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。



class Solution(object):
    def combinationSum(self, candidates, target):

        length = len(candidates)   ####列表长度

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
#给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。回溯加剪枝

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

                if index > begin and candidates[index - 1] == candidates[index]:  ###重复
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


#不含重复元素的整数数组 nums，返回该数组所有可能的子集  78
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

#####给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集90
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)
        if size == 0:
            result.append([])
            return

        nums.sort()

        def backtrack(path, start):
            result.append(path)  # 每一片叶子都是我要的答案
            if start == size:
                return
            for i in range(start, size):
                if i > start and nums[i - 1] == nums[i]:  # 保证同层不重复，异层可以相同
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
            if res < 0:        ####缺了这个，就一直在跑
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
            if mark[i][j] == 1:   ##走过的不能再走的意思吗？
                return False
            if board[i][j] == word[0]:
                mark[i][j] = 1
                #函数有返回值要先赋值。
                fanhuiz = backtrack(i+1, j, mark, word[1:]) or backtrack(i-1, j, mark, word[1:]) or backtrack(i, j-1, mark, word[1:]) or backtrack(i, j+1, mark, word[1:])
                #这个不能直接if not (backtrack(i+1, j, mark, word[1:]) or backtrack(i-1, j, mark, word[1:]) or backtrack(i, j-1, mark, word[1:]) or backtrack(i, j+1, mark, word[1:]))
                if not fanhuiz:
                    mark[i][j] = 0 #回溯，因为这个点没走下去，因此这个点相当于没走
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
        columns = set()  #列
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n  #行
        backtrack(0)
        return solutions

solutions = Solution().solveNQueens(4)