class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)
        resultss = [1] * len(nums)
        rresult = [1] * len(nums)

        prefix = 1
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]
            
            
        suffix = 1
        for j in range(len(nums) - 2, -1, -1):
            resultss[j] = resultss[j+1] * nums[j + 1]

        for k in range(len(nums)):
            print(result[k], resultss[k])
            rresult[k] = result[k] * resultss[k]
        
        return rresult