'''
两个指针的滑动
两个循环
'''


def long(str):
    ####记录独特的字符
    occ = set()
    #字符串的长度
    n = len(str)
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:         #左指针向右移动一格，移除一个字符
            occ.remove(str[i-1])
        while rk + 1 < n and str[rk+1] not in occ:  #######不断地移动右指针

            occ.add(str[rk+1])
            rk += 1

        ans = max(ans, rk-i+1)
