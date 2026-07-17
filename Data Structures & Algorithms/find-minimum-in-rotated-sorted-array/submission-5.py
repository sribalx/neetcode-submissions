class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[0] < nums[r]:
            return nums[0]
        
        while (l < r):
            mid = l + (r - l) // 2
            #print (f"l is {l}, r is {r}, mid is {mid}")
            if nums[mid] < nums [r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
        
        return nums[l]