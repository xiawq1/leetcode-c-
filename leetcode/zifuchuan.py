#coding:gbk


#242
class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False
        hash = collections.defaultdict()
        for i in s:
            hash[i] = hash.get(i, 0) + 1
        for j in t:
            hash[j] = hash.get(j, 0) - 1
        for k, v in hash.items():
            if v != 0:
                return False
        return True

#205



#647
class Solution:
    def countSubstrings(self, s):
        dp = [1 for i in range(len(s))]
        for i in range(1, len(s)):
            for j in range(i):
                if s[i] == s[j] and s[j+1] == s[i-1]:
                    dp[j] += 1
        sum = 0
        for i in dp:
            sum += i
        return sum

#696



#224  基本计算器
class Solution:

    def evaluate_expr(self, stack):
        res = stack.pop() if stack else 0

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s):

        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():

                # Forming the operand - in reverse order.
                operand = (10**n * int(ch)) + operand
                n += 1

            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0

                if ch == '(':
                    res = self.evaluate_expr(stack)
                    stack.pop()

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)

                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)


Solution().calculate("(1+(4+5+2)-3)+(6+8)")

#409
class Solution:
    def longestPalindrome(self, s):
        ans = 0
        count = collections.Counter(s)   ##计算每个单词出现的平率
        for v in count.values():
            ans += v // 2 * 2   ##左右各放相等的字符
            if ans % 2 == 0 and v % 2 == 1:  #如果ans为偶数，v是奇数，可以将多余的作为中心。此时ans已经为奇数，接下来就不会跑这段代码了
                ans += 1
        return ans



#3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        n = len(s)
        res = 0
        rk = 0
        for i in range(n):
            if i > 0:
                hash.remove(s[i-1])
            while rk < n and s[rk] not in hash:
                hash.add(s[rk])
                rk += 1
            res = max(res, rk - i)
        return res

#5
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
















