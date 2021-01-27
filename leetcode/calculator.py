#coding:gbk

##224       ʵ��+��-�����Ұ�������

class Solution():
    def calculate(self, s):
        res = 0
        num = 0
        sign = 1
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c == "(":
                j = i
                cnt = 0
                while i < n:
                    if s[i] == "(":
                        cnt += 1
                    if s[i] == ")":
                        cnt -= 1
                    if cnt == 0:
                        break
                    i += 1
                num = self.calculate(s[j+1:i])
            if s[i] == "+" or s[i] == "-" or i == n - 1:
                res += sign * num
                num = 0
                sign = 1 if s[i] == "+" else -1
            i += 1
        return res
Solution().calculate("(1+(4+5+2)-3)+(6+8)")

#227  +,-,*,/
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        op = "+"
        n = len(s)
        res = 0
        num = 0
        stack = []
        for i in range(n):
            if s[i] <= "9" and s[i] >= "0":
                num = num * 10 + int(s[i])

            if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/' or i == n - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == "*":
                    t = stack.pop(-1) * num
                    stack.append(t)
                else:
                    if stack[-1] > 0:
                        t = stack.pop(-1) // num
                    else:
                        t = -(-stack.pop(-1) // num)
                    stack.append(t)
                num = 0
                op = s[i]
        while stack:
            # stack.pop(-1) Ҳ��
            res = res + stack.pop(0)
        return res

#772
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        op = "+"
        n = len(s)
        res = 0
        num = 0
        stack = []
        i = 0
        while i < n:
            if s[i] >= "0" and s[i] <= "9":
                num = num * 10 + int(s[i])
            elif s[i] == "(":
                j = i
                cnt = 0
                while i < n:
                    if s[i] == "(":
                        cnt += 1
                    if s[i] == ")":
                        cnt -= 1
                    if cnt == 0:
                        break
                        # break��i+1���ټ���
                    i += 1
                num = self.calculate(s[j + 1:i])

            if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/' or i == n - 1:
                # op����һ�������Ĳ�����
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == "*":
                    t = stack.pop(-1) * num
                    stack.append(t)
                else:
                    # ���python�ĸ�����ȡ��
                    if stack[-1] > 0:
                        t = stack.pop(-1) // num
                    else:
                        t = -(-stack.pop(-1) // num)
                    stack.append(t)
                num = 0
                op = s[i]
            i += 1
        while stack:
            # stack.pop(-1) Ҳ��
            res = res + stack.pop(0)
        return res