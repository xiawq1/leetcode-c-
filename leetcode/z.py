# coding=gbk
'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
'''

class Solution:
    def convert(self, s, numrows):
        if numrows < 2:return s
        res = ['' for _ in range(numrows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numrows-1:flag = -flag
            i += flag
        return ''.join(res)
s = Solution()
a = s.convert('LEETCODEISHIRING', 4)
print(a)