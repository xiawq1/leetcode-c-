'''
动态规划问题
到达某个格子的路径有这一格子的左和上面的格子决定
'''


class Solution:
    def uniquePaths(self, m, n):
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]
a = Solution().uniquePaths(7, 4)
print(a)