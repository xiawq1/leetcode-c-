class solution(object):
    def length_string(self, s):
        s = list(s)
        a = []
        for i in range(len(s)):
            if s[i] in a:
                length = i
                break
            else:
                a.append(s[i])
        return length
s = 'pwwkew'
o = solution()
length = o.length_string(s)

print(length)
