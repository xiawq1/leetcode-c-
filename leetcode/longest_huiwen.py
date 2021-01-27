'''
5ֻ�� s[i+1:j-1]�ǻ��Ĵ������� s �ĵ� i�� j����ĸ��ͬʱ��s[i:j]���ǻ��Ĵ�
'''
class Solution:
    def longest(self, s):
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = ''
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True   #�Խ���
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
