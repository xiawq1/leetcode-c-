#coding:gbk
'''

��������
'''

from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        findOut = defaultdict(int)   #û���ҵ�keyʱҲ���ᱨ��
        for letter in t:
            findOut[letter] += 1
        index1 = 0
        index2 = 0
        counter = len(t)
        length = len(s)
        min_len = float("inf")
        result = ""
        while index2 < length:
            if findOut[s[index2]] >= 1:
                counter -= 1
            findOut[s[index2]] -= 1  ##��Ӧ
            index2 += 1
            while counter == 0:
                if min_len > index2 - index1:
                    min_len = index2 - index1
                    result = s[index1 : index2]
                if findOut[s[index1]] == 0:
                    counter += 1
                findOut[s[index1]] += 1   ##  ��Ӧ���Է�����t�������ַ���Ӱ��
                index1 += 1
        return result

Solution().minWindow("ADOBECODEBANC", "ABC")
