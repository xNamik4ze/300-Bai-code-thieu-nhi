class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lis = [0] + flowerbed + [0]
        for i in range(1, len(lis) - 1):
            if n == 0:
                return True
            if lis[i - 1] == lis[i] == lis[i + 1] == 0:
                n -= 1
                lis[i] = 1
        return n == 0