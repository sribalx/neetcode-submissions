class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_cookers = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cookers.append(i)
                continue
            product = product * nums[i]
        
        s = len(zero_cookers)
        result = []
        for j in range(len(nums)):
            if nums[j] == 0:
                if s == 1:
                    result.append(int(product))
                    continue
                if s != 1:
                    result.append(0)
                    continue
            if s > 0:
                result.append(0)
                continue
            else:
                result.append(int(product/nums[j]))
        
        return result

            

