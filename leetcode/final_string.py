
'''
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
'''

def get_final_length(s):
    s = s.strip().split()
    s_final = s[-1]
    return s_final