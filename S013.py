class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {
            'I' : 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        for i in range(len(s)):
            value = roman_value[s[i]]
            if i < len(s) - 1 and value < roman_value[s[i + 1]]:
                num -= value
            else:
                num += value
        return num
