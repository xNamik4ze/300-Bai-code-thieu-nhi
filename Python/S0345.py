class Solution:
    def reverseVowels(self, s: str) -> str:
        lis = list(s)
        vowels = set("aeiouAEIOU")
        l, r = 0, len(lis) - 1
        while l < r:
            while lis[l] not in vowels and l < r: 
                l += 1
            while lis[r] not in vowels and l < r:
                r -= 1
            lis[l], lis[r] = lis[r], lis[l]
            l += 1
            r -= 1
        return "".join(lis)