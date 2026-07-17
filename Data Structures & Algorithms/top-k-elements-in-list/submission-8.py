from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a hashmap with number as key
        # create a hashmap with frequency as key. at most can have n frequency
        # iterate from above on the hashmap to add to list and then when it hits k

        result = []
        n = len(nums)
        count = defaultdict(int)
        freq = defaultdict(list)

        for num in nums:
            count[num] += 1
        
        for number, frequency in count.items():
            freq[frequency].append(number)

        for i in range(n, 0, -1):
            for digit in freq[i]:
                result.append(digit)
                if len(result) == k:
                    return result



        

     
