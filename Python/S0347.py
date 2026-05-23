class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        lis = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            lis[freq].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for num in lis[i]: 
                result.append(num)
                if len(result) == k:
                    return result
                
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sorted(count, key=count.get, reverse=True)[:k]