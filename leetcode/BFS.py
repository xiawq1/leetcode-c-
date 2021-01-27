#coding:gbk
import collections
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n, queue = len(A), []
        def dfs(x,y):
            A[x][y] = -1
            queue.append((x,y))
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0<=i<n and 0<=j<n and A[i][j] == 1:
                    dfs(i, j)
        def find_first_island():
            for i in range(n):
                for j in range(n):
                    if A[i][j] == 1:
                        dfs(i,j)
                        return
        find_first_island()
        count = 0
        while queue:
            t = []
            for x, y in queue:
                for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0<=i<n and 0<=j<n:
                        if  A[i][j]==1:
                            return count
                        elif A[i][j]==0:
                            A[i][j] = -1
                            t.append((i, j))
            count += 1
            queue = t
Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])