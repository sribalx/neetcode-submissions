class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_diff = 0
        lowest_no = 10000
        for num in prices:
            lowest_no = min(lowest_no, num)
            max_diff = max(max_diff, num - lowest_no)

        return max_diff