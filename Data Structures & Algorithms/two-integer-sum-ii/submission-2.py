from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        result = []
        
        l = 0
        r = len(numbers) - 1
    
        while numbers[r] + numbers[l] > target:
            r -= 1

        print(l, r)
        
        while l < r:
            temp_sum = numbers [l] + numbers [r]

            if temp_sum > target:
                r -= 1
            
            elif temp_sum < target:
                l += 1
            
            else:
                result.append(l + 1)
                result.append(r + 1)
                return result
        
        return []
            
        
