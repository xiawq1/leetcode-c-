#coding:gbk

##�������

class Solution:
    def generate(self, numRows):
        dp = [[1]*(i + 1) for i in range(numRows)]


        n = 2 # ��Ϊǰ���е�������Ƕ���1,�������Ǵӵ����п�ʼ�޸�

        # ���numRows��С��3�ģ����õ���Ӵ���������whileѭ��

        while n < numRows: # �ӵ����п�ʼ����ÿһ��
            for i in range(1, len(dp[n]) - 1):

                dp[n][i] = dp[n - 1][i - 1] + dp[n - 1][i]


            n += 1 # n�ǵü�һӴ��������һ��

        return dp
dp = Solution().generate(5)
print(dp)
