class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
def phpneLetter(digits):
    if not digits:
        return []
    keyboard = {
       "2":'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    res = []
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return keyboard[digits]
    restult = phpneLetter(digits[1:])   ######µÝ¹éÂð£¿
    for i in restult:
        for j in keyboard[digits[0]]:
            res.append((j+i))

    return res

print(phpneLetter('345'))



