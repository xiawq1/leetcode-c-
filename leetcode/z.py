# coding=gbk
'''
��һ�������ַ������ݸ������������Դ������¡������ҽ��� Z �������С�
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