#coding:gbk
'''

滑动窗口
'''

from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        findOut = defaultdict(int)   #没有找到key时也不会报错
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
            findOut[s[index2]] -= 1  ##对应
            index2 += 1
            while counter == 0:
                if min_len > index2 - index1:
                    min_len = index2 - index1
                    result = s[index1 : index2]
                if findOut[s[index1]] == 0:
                    counter += 1
                findOut[s[index1]] += 1   ##  对应，以防除了t中其它字符的影响
                index1 += 1
        return result

Solution().minWindow("ADOBECODEBANC", "ABC")
