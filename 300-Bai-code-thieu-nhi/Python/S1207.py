class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for x in arr:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        freq = counts.values()
        return len(freq) == len(set(freq))