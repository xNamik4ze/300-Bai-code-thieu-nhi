class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = 0
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                total = prices[i] - min
                if total > max:
                    max = total
        if max > 0:
            return max
        else:
            return 0
