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
            if len(path) == len(tickets) + 1:  # ��������
                return True
            ticket_dict[cur_from].sort()   #����
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)  # ɾ����ǰ�ڵ�
                path.append(cur_to)  # ��ѡ��
                if backtrack(cur_to):  # ������һ�������
                    return True
                path.pop()  # ȡ��ѡ��
                ticket_dict[cur_from].append(cur_to)  # �ָ���ǰ�ڵ�
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