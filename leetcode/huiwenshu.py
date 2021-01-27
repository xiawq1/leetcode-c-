# coding=gbk
"""
判断一个整数是否是回文数
"""

def judge_huiwen(i):
    flag = False
    str_i = str(i)

    if i == int(str_i[::-1]):
        flag = True
    return flag

a = judge_huiwen(121)
print(a)



