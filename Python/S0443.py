class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            count = j - i
            chars[index] = chars[i]
            index += 1
            i = j
            if count > 1:
                s = str(count)
                for digit in s:
                    chars[index] = digit
                    index += 1
        return index