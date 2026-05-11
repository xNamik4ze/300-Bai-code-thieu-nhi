class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        rem = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or rem:
            val1 = int(a[i]) if i >= 0 else 0
            val2 = int(b[j]) if j >= 0 else 0
            total = val1 + val2 + rem
            res.append(str(total % 2))
            rem = total // 2
            i -= 1 
            j -= 1
        return ''.join(res[::-1])