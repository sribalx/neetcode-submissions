class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result_list = []
        low = 1
        high = max(piles)
        while low <= high:
            hours_taken = 0
            mid_k = low + (high - low) // 2
            #print(f"mid_k is {mid_k}")
            for bananas in piles:
                hours_taken += -(-bananas//mid_k)
            if hours_taken <= h:
                result_list.append(mid_k)
                high = mid_k - 1
            elif hours_taken > h:
                low = mid_k + 1
        
        return min(result_list)