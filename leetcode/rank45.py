# coding=utf-8

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