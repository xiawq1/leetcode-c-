# coding=gbk
"""
�ж�һ�������Ƿ��ǻ�����
"""

def judge_huiwen(i):
    flag = False
    str_i = str(i)

    if i == int(str_i[::-1]):
        flag = True
    return flag

a = judge_huiwen(121)
print(a)



