class Solution:
    def trap(self, height: List[int]) -> int:
        # idea is that as i move from left to right, if 
        '''
        base_res = []
        l = 0
        r = len(height) - 1

        while(l > r):
            area = (r - 1 - 1) * (min(height[l], height[r]))
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        '''
        # save the heighest points to the left and right of each column, 
        # and then process later

        base_res = [0] * len(height)
        sum = 0
        for i in range(1, len(height) - 1):
            base_res[i] = max(min(max(height[0:i]), max(height[i+1:len(height)])) - height[i], 0)

        for i in range(len(base_res)):
            sum += base_res[i]

        return sum
         
        