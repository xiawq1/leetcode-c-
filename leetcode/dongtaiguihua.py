# #coding:gbk
# #5������Ӵ�
# #ֻ�� s[i+1:j-1]�ǻ��Ĵ������� s�ĵ� i�� j����ĸ��ͬʱ��s[i:j]�Ż��ǻ��Ĵ�
#
# class Solution:
#     def longestPalindrome(self, s):
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         ans = ""
#         # ö���Ӵ��ĳ��� l+1
#         for l in range(n):
#             # ö���Ӵ�����ʼλ�� i����������ͨ�� j=i+l �õ��Ӵ��Ľ���λ��
#             for i in range(n):
#                 j = i + l
#                 if j >= len(s):
#                     break
#                 if l == 0:
#                     dp[i][j] = True
#                 elif l == 1:
#                     dp[i][j] = (s[i] == s[j])
#                 else:
#                     dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
#                 if dp[i][j] and l + 1 > len(ans):
#                     ans = s[i:j+1]   #�õ����Ĵ�
#         return ans
#
# ##��������53
#
# class Solution3():
#     def find_lianxu(self, nums):
#         dp = 0
#         result = nums[0]
#         for i in range(len(nums)):
#             dp = max(dp+nums[i], nums[i])
#             if result < dp:
#                 result = dp
#         return result
# # [-2,1,-3,4,-1,2,1,-5,4]
#
# #62 һ��������λ��һ�� m x n ��������Ͻǣ�������ÿ��ֻ�����»��������ƶ�һ������������ͼ�ﵽ��������½�
# class Solution11:
#     def uniquePaths(self, m, n):
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         for j in range(n):           ###��0�У���0��
#             dp[0][j] = 1
#         for i in range(m):
#             dp[i][0] = 1
#         for i in range(1,m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i][j-1]+dp[i-1][j]
#         return dp[m-1][n-1]   ##################�ӵ�0�п�ʼ������Ҫ��һ
# aa = Solution11().uniquePaths(7,3)
# print(aa)
# #63   ���ϰ���
# class Solution22:
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         for j in range(n):
#             if obstacleGrid[0][j] == 0:
#                 dp[0][j] = 1
#             else:
#                 dp[0][j] = 0
#
#                 if j < n - 1:
#                     for jj in range(j, n):
#                         dp[0][jj] = 0
#                 break
#
#         for i in range(m):
#             if obstacleGrid[i][0] == 0:
#                 dp[i][0] = 1
#             else:
#                 dp[i][0] = 0
#
#                 if i < m - 1:
#                     for ii in range(i, m):
#                         dp[ii][0] = 0
#                 break
#
#         for i in range(1, m):
#             for j in range(1, n):
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
#
#         return dp[m - 1][n - 1]
#
# ss = Solution22().uniquePathsWithObstacles([
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ])
# print(ss)
#
# ##��С·����
# class Solution4():
#     def min_path(self, grid):
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = grid[0][0]
#         for i in range(1, m):
#             dp[i][0] = grid[i][0] + dp[i - 1][0]
#         for j in range(1, n):
#             dp[0][j] = grid[0][j] + dp[0][j - 1]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
#
#         return dp[m - 1][n - 1]
#
# #70 ��¥��
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n==1:
#             return 1
#         if n==2:
#             return 2
#         dp = [0 for _ in range(n+1)]
#         dp[1]=1
#         dp[2]=2
#         for i in range(3, n+1):
#             dp[i] = dp[i-1]+dp[i-2]
#         return dp[n]
#
#
# #90���뷽��
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         length = len(s)
#         if length == 0:
#             return 0
#         if length == 1:
#             if s[0] == "0":
#                 return 0
#             else:
#                 return 1
#         dp = [0 for _ in range(length + 1)]
#         dp[0] = 1
#
#         for i in range(1, length + 1):
#             if s[i - 1] == '0':
#                 dp[i] = 0
#             else:
#                 dp[i] = dp[i - 1]
#             if i > 1 and (s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6")):
#                 dp[i] += dp[i - 2]
#
#         return dp[-1]
#
# #120��������С·����
#
# class Solution:
#     def minimumTotal(self, triangle):
#         rows = len(triangle)
#         dp = [[0 for _ in range(rows)] for _ in range(rows)]
#         for i in range(rows):
#             if i == 0:
#                 dp[0][0] = triangle[0][0]
#             for j in range(len(triangle[i])):
#                 if i == 0 and j == 0:
#                     dp[i][j] = triangle[0][0]
#                 elif j == 0:
#                     dp[i][j] = dp[i - 1][j] + triangle[i][j]   #######��һ��
#                 elif j == len(triangle[i]) - 1:
#                     dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]   ######���������ε����У���һ�б���һ�ж�һ��
#                 else:
#
#                     dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
#
#         return min(dp[-1])
#
# #���Ʊ�����ʱ��
# class Solution:
#     def maxProfit(self, prices):
#         length = len(prices)
#         if length == 0:
#             return 0
#         dp = [0 for _ in range(length)]
#         min_price = prices[0]
#         for i in range(length):
#             if i==0:
#                 dp[i]=0
#             else:
#                 min_price = min(min_price, prices[i])
#                 dp[i]= max(dp[i-1], prices[i]-min_price)
#         return max(dp)
#
# #62
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[0 for i in range(n)] for i in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if i == 0:
#                     dp[0][j] = 1
#                 elif j == 0:
#                     dp[i][0] = 1
#                 else:
#                     dp[i][j] = dp[i][j-1] + dp[i-1][j]
#         return dp[m-1][n-1]
# #63
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         dp = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
#         for i in range(0, len(obstacleGrid[0])):
#             if obstacleGrid[0][i] == 0:
#                 dp[0][i] = 1
#             else:
#                 dp[0][i] = 0
#                 if i < len(obstacleGrid[0])-1:
#                     for j in range(i+1, len(obstacleGrid[0])):
#                         dp[0][j] = 0
#                     break
#         for i in range(0, len(obstacleGrid)):
#             if obstacleGrid[0][i] == 0:
#                 dp[i][0] = 1
#             else:
#                 dp[i][0] = 0
#                 if i < len(obstacleGrid)-1:
#                     for j in range(i+1, len(obstacleGrid)):
#                         dp[j][0] = 0
#                     break
#
#         for i in range(1, len(obstacleGrid)):
#             for j in range(1, len(obstacleGrid[0])):
#
#
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     dp[i][j] = dp[i][j-1] + dp[i-1][j]
#
#         return dp[-1][-1]
#
# #55
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         m = len(nums)
#         dp = [False for _ in range(m)]
#         if m == 0:
#             return True
#         dp[0] = True
#         for i in range(1, m):
#             for j in range(i):
#                 if nums[j] >= i - j and dp[j]:
#                     dp[i] = True
#                     break
#         return dp[m - 1]
# #300
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         dp = []
#         for i in range(len(nums)):
#             dp.append(1)
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)
# #354
# # ������������㷨�޷�ͨ��
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         envelopes.sort()
#         # envelopes.sort(key=lambda x: x[0])
#         size = len(envelopes)
#         if size == 0:
#             return 0
#
#         dp = [0 for _ in range(size)]
#
#         dp[0] = 1
#
#         for i in range(1, size):
#             dp[i] = 1
#             for j in range(i):
#                 if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#
#         return max(dp)
#
# #152
#
# #�ö�̬�滮��������dp[i]��ʾ��i��β���������е����ֵ����i��βʱ�˿̲�����С�������ֵ�����ά��max_value��min_value��
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return
#         dp = [0 for _ in range(len(nums))]
#         dp[0] = nums[0]
#         max_value = nums[0]
#         min_value = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = max(max_value * nums[i], min_value * nums[i], nums[i])
#             min_value = min(max_value * nums[i], min_value * nums[i], nums[i])
#             max_value = dp[i]
#         # print(dp)
#         return max(dp)
# #64
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         if not grid or not grid[0]:
#             return 0
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[0 for i in range(n)] for i in range(m)]
#         dp[0][0] = grid[0][0]
#         for i in range(1, m):
#             dp[i][0] = dp[i-1][0] + grid[i][0]
#         for j in range(1, n):
#             dp[0][j] = dp[0][j-1] + grid[0][j]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#
#         return dp[-1][-1]
#
#
# #515 lintcode
# class Solution:
#     """
#     @param costs: n x 3 cost matrix
#     @return: An integer, the minimum cost to paint all houses
#     """
#
#     def minCost(self, costs):
#         # write your code here
#         m = len(costs)   #������Ŀ
#         if m == 0:
#             return 0
#         n = len(costs[0])  ##ÿ�䷿Ⱦɫ�ļ۸�
#         if n == 0:
#             return 0
#
#         dp = [[0 for _ in range(n)] for _ in range(m + 1)]
#
#         for i in range(m + 1):
#             for j in range(n):
#                 if i == 0:
#                     dp[i][j] = 0
#                     continue
#                 dp[i][j] = float('inf')
#                 for k in range(n):
#                     if k != j:
#                         dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])
#         return min(dp[m])
#
#
# class Solution:
#     """
#     @param costs: n x k cost matrix
#     @return: an integer, the minimum cost to paint all houses
#     """
#
#     def minCostII(self, costs):
#         # write your code here
#         m = len(costs)
#         if m == 0:
#             return 0
#         n = len(costs[0])
#         if n == 0:
#             return 0
#
#         dp = [[0 for _ in range(n)] for _ in range(m + 1)]
#         for i in range(n):
#             dp[0][i] = 0
#
#         for i in range(1, m + 1):
#             min_v = float('inf')
#             sec_v = float('inf')
#             min_i = 0
#             sec_i = 0
#             # �ȼ���dp[i-1]����Сֵ�ʹ�Сֵ
#             for j in range(n):
#                 if dp[i - 1][j] < min_v:
#                     sec_v = min_v
#                     sec_i = min_i
#                     min_v = dp[i - 1][j]
#                     min_i = j
#                     continue
#                 if dp[i - 1][j] < sec_v:
#                     sec_v = dp[i - 1][j]
#                     sec_i = j
#             # �ټ���dp[i][j]
#             for j in range(n):
#                 if j != min_i:
#                     dp[i][j] = min_v + costs[i - 1][j]
#                 if j == min_i:
#                     dp[i][j] = sec_v + costs[i - 1][j]
#
#         return min(dp[m])
#

#198
class Solution:
    def rob(self, nums):
        n = len(nums)
        dp = [0 for i in range(n)]
        if not nums:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(dp)

#213
class Solution:
    def rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        dp = [0 for i in range(size)]

        dp[0] = 0
        nums1 = nums[:size-1]
        for i in range(1, size):
            if i == 1:
                dp[i] = nums1[0]
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums1[i - 1])
        max_value = dp[-1]
        nums2 = nums[1:]
        for i in range(1, size):
            if i == 1:
                dp[i] = nums2[0]
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums2[i - 1])

        max_value = max(max_value, dp[-1])
        return max_value

#121
class Solution():
    def MaxProfit(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        min_value = float('inf')
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            min_value = min(min_value, nums[i-1])
            if min_value < nums[i-1]:
                dp[i] = max(dp[i], nums[i-1]-min_value)
        return dp[-1]

class Solution:
    def maxProfit(self, prices):
        size = len(prices)
        if size == 0:
            return 0

        dp = [0 for _ in range(size+1)]
        dp[0] = 0
        dp[1] = 0
        min_value = float('inf')
        for i in range(2, size+1):
            min_value = min(min_value, prices[i-2])
            if prices[i-1] >= min_value:
                dp[i] = prices[i-1] - min_value
                min_value = prices[i-1]
        return sum(dp)

#279
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # write your code here
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            dp[i] = float('inf')
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[-1]


#132

class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        def isPalin(s):  # ���ö�̬�滮����ǲ��ǻ��Ĵ���
            size = len(s)
            dp = [[False for _ in range(size)] for _ in range(size)]
            for j in range(size):
                i = j
                while i >= 0 and j < size and s[i] == s[j]:
                    dp[i][j] = True
                    i -= 1
                    j += 1
            for j in range(1, size):
                i = j - 1
                while i >= 0 and j < size and s[i] == s[j]:
                    dp[i][j] = True
                    i -= 1
                    j += 1

            return dp

        dp1 = isPalin(s)

        dp2 = [0 for _ in range(size + 1)]
        dp2[0] = 0

        for j in range(1, size + 1):
            min_value = float('inf')
            for i in range(j):
                if dp1[i][j - 1]:  # ע��Ҫ��isPalin�ó��ľ����Ӧ
                    min_value = min(min_value, dp2[i] + 1)
            dp2[j] = min_value

        return dp2[size] - 1

#413
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        dp = [0 for i in range(n)]
        sum_ans = 0
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
                sum_ans += dp[i]
        return sum_ans

#64
import collections
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        queue = collections.deque()
        visited = [[0] * N for _ in range(M)]
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                if matrix[x][y] == 1:
                    res[x][y] = step
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= M or newy < 0 or newy >= N or visited[newx][newy] == 1:
                        continue
                    queue.append((newx, newy))
                    visited[newx][newy] = 1
            step += 1
        return res

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # ��ʼ����̬�滮�����飬���еľ���ֵ������Ϊһ���ܴ����
        dist = [[10**9] * n for _ in range(m)]
        # ��� (i, j) ��Ԫ��Ϊ 0����ô����Ϊ 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # ֻ�� ˮƽ�����ƶ� �� ��ֱ�����ƶ���ע�⶯̬�滮�ļ���˳��
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # ֻ�� ˮƽ�����ƶ� �� ��ֱ�����ƶ���ע�⶯̬�滮�ļ���˳��
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # ֻ�� ˮƽ�����ƶ� �� ��ֱ�����ƶ���ע�⶯̬�滮�ļ���˳��
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        # ֻ�� ˮƽ�����ƶ� �� ��ֱ�����ƶ���ע�⶯̬�滮�ļ���˳��
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist

#221
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
        max_size = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
                    max_size = max(max_size, dp[i][j])
        return max_size * max_size

#279
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]

        for i in range(1, n+1):
            for j in range(1, n):
                if j * j <= i:
                    dp[i] = min(dp[i], dp[i-j*j] + 1);
                else:
                    break
        return dp[n]

#300    [10,9,2,5,3,7,101,18]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        dp = [1 for i in range(n)]
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:

                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])


        return res

#1143     text1 = "abcde", text2 = "ace"   3
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

