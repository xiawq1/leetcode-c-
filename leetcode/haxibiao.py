#coding:gbk


#332
class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        ticket_dict = defaultdict(list)
        for item in tickets:
            ticket_dict[item[0]].append(item[1])

        path = ['JFK']

        def backtrack(cur_from):
            if len(path) == len(tickets) + 1:  # 结束条件
                return True
            ticket_dict[cur_from].sort()   #排序
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)  # 删除当前节点
                path.append(cur_to)  # 做选择
                if backtrack(cur_to):  # 进入下一层决策树
                    return True
                path.pop()  # 取消选择
                ticket_dict[cur_from].append(cur_to)  # 恢复当前节点
            return False

        backtrack('JFK')
        return path


#303
class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0 for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            self.dp[i] = self.dp[i-1] + nums[i-1]
        return self.dp

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i-1]



#304
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: