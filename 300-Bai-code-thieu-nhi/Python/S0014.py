class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s1 = strs[0]
        s2 = strs[-1]
        res = []
        n1 = len(s1)
        n2 = len(s2)
        count = 0
        while count < min(n1, n2):
            if s1[count] == s2[count]:
                res.append(s1[count])
            else:
                return "".join(res)
            count += 1
        return "".join(res) 