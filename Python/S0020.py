class Solution:
    def isValid(self, s: str) -> bool:
        s_value = {
            '(' : 1, ')' : 4,
            '[' : 2, ']' : 5,
            '{' : 3, '}' : 6
        }
        lis = []
        for i in range(len(s)):
            value = s_value[s[i]]
            if value < 4:
                lis.append(value)
            elif lis and value > 3 and value - lis[-1] == 3:
                lis.pop()
            else: return False
        if lis: return False
        else: return True 