class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        k = 0
        n = len(s) - 1
        while k <= n:
            if not s[k].isalpha():
                k += 1
            elif not s[n].isalpha():
                n -= 1
            elif s[k] != s[n]:
                return False
            else:
                k += 1
                n -= 1
        return True