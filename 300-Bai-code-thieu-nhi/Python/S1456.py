class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cur = 0
        for i in range(k):
            if s[i] in vowels:
                cur += 1
        if cur == k: 
            return cur
        max_val = cur
        for i in range(k, len(s)):
            if s[i] in vowels:
                cur += 1
            if s[i-k] in vowels:
                cur -= 1
            if cur == k:
                return cur
            elif cur > max_val:
                max_val = cur
        return max_val