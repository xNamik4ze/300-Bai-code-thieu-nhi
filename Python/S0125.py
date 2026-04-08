class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        k = 0
        n = len(s) - 1
        while k <= n:
            if not s[k].isalnum():
                k += 1
            elif not s[n].isalnum():
                n -= 1
            elif s[k] != s[n]:
                return False
            else:
                k += 1
                n -= 1
        return True