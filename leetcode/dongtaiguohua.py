#coding:gbk

# 53����һ������f(n)���Ե�n����Ϊ������������е����ͣ�����һ�����ƹ�ϵf(n) = max(f(n-1) + A[n], A[n])
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = 0
        result = nums[0]
        for i in range(len(nums)):
            dp = max(dp+nums[i], nums[i])
            if result<dp:
                result = dp
        return result

#һ��������λ��һ�� m x n ��������Ͻǣ�������ÿ��ֻ�����»��������ƶ�һ������������ͼ�ﵽ��������½ǣ������ܹ��ж�������ͬ��·��


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]