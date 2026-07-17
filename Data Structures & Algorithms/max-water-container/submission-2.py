class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # trying to maximise for (r-l) * (min(heights[l], heights[r]))
    
        max_area = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            print(heights[l], heights[r], max_area)
            temp_area = (r-l) * (min(heights[l], heights[r]))
            if temp_area > max_area:
                max_area = temp_area
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else: 
                l += 1

        
        return max_area