#slower but less memory (Integrated carry)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)
        for i in range(n1 - 1, - 1, -1):
            for j in range(n2 - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                total = product + res[i+j+1]
                res[i+j+1] = total % 10
                res[i+j] += total // 10 
        ans = "".join(map(str, res))
        return ans.lstrip('0')

#faster but more memory (Post-process carry)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)
        for i in range(n1 - 1, - 1, -1):
            for j in range(n2 - 1, -1, -1):
                res[i+j+1] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        for i in range(n1 + n2 - 1, 0, -1):
            res[i-1] += res[i] // 10
            res[i] %= 10
        ans = "".join(map(str, res))
        return ans.lstrip('0')