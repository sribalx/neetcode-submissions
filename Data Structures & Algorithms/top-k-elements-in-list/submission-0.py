from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        

        for i in range(k):
            largest_value = 0
            largest_key = 0
            for key, value in hashmap.items():
                if value > largest_value:
                    largest_value = value
                    largest_key = key
            
            result.append(largest_key)
            del hashmap[largest_key]

        return result