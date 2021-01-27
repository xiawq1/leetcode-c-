#coding=gbk
#给你一个字符串 s 和一个字符规律 p, 支持 '.' 和 '*' 的正则表达式匹配


'''
动态规划，用 f[i][j] 表示 s的前 i 个字符与 p 中的前 j 个字符是否能够匹配
'''

class Solution:
    def ismatch(self, s, p):
        m = len(s)
        n = len(p)
        def matches(i, j):
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]
s = "aab"
p = "c*a*b"
a = Solution()
cc = a.ismatch(s, p)
print(cc)