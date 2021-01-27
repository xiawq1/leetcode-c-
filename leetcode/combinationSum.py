# coding=utf-8
'''
回朔
'''

class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx, res):
            if idx >= len(candidates) or res >= target:
                if res == target:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res + candidates[idx])
            temp.pop()
            recursion(idx + 1, res)
        recursion(0, 0)
        return ans
aa = Solution().combinationSum([2,3,6,7], 7)


class Solution:
    def letterCombination(self, digits):

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],

                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        res = []  # 存放组合结果

        def backtrack(combination, next_digits):  # 回溯函数
            # combination目前已经产生的组合，next_digits:输入的下一个字符
            if len(next_digits) == 0:  # 递归出口
                res.append(combination)
            else:
                for i in phone[next_digits[0]]:
                    backtrack(combination + i, next_digits[1:])  # 递归实现回溯

        if digits:
            backtrack('', digits)  # 初始化
        return res

a = Solution().letterCombination(['2', '3', '4'])


class Solution:
    def permute(self, nums):

        res = []  # 存放组合结果
        size = len(nums)

        def backtrack(combination, nums):
            # combination目前已经产生的组合，nums为剩下的数组
            # 递归出口
            # 递归的结束一定 要有return
            if len(combination) == size:
                res.append(combination)
                return  # 注意
            for i in range(len(nums)):
                backtrack(combination + [nums[i]], nums[:i] + nums[i + 1:])  # 递归回溯

        backtrack([], nums)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))
