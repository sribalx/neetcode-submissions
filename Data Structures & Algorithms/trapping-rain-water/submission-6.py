class Solution:
    def trap(self, height: List[int]) -> int:

        sum = 0
        l = 0
        r = len(height) - 1
        largest_l = 0
        largest_r = 0

        while l < r:
            temp = 0
            largest_l = max(largest_l, height[l])
            largest_r = max(largest_r, height[r])
            
            if height[r] <= height[l]:
                temp = min(largest_l, largest_r) - height[r]
                r -= 1
            
            elif height[r] > height[l]:
                temp = max(min(largest_l, largest_r) - height[l], 0)
                l += 1
            
            sum += temp

        return sum




        
        