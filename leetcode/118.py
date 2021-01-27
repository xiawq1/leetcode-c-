#coding:gbk

##杨辉三角

class Solution:
    def generate(self, numRows):
        dp = [[1]*(i + 1) for i in range(numRows)]


        n = 2 # 因为前两行的杨辉三角都是1,所以我们从第三行开始修改

        # 如果numRows是小于3的，不用担心哟，不会进入while循环

        while n < numRows: # 从第三行开始遍历每一行
            for i in range(1, len(dp[n]) - 1):

                dp[n][i] = dp[n - 1][i - 1] + dp[n - 1][i]


            n += 1 # n记得加一哟，进入下一行

        return dp
dp = Solution().generate(5)
print(dp)
