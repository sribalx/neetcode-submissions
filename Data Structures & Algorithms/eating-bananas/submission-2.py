import numpy as np
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #if h == len(piles):
        #   return max(piles)
        
        l, r = 1, max(piles)
        result = r

        while l<=r:
            mid = (l+r) // 2
            tTime = 0

            for p in piles:
                tTime += np.ceil(p/mid)

            if tTime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return res
        


        

            
    # upper bound is the max(piles)
    # lower bound is ceil(sum(piles)/h)
    # 