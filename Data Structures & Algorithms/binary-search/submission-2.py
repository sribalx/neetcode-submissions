class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(0, len(nums) - 1, nums, target)
        
    def binarysearch(self, l, r , nums, target):    
        if l > r:
            return -1
        
        test = l + (r-l)//2

        if nums[test] == target:
            return test
        elif nums[test] < target:
            return self.binarysearch(test + 1, r, nums, target)
        elif nums[test] > target:
            return self.binarysearch(l, test - 1, nums, target)
        