from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hash1 = {}
        longest_len = 0
        for num in nums:
            hash1[num] = num
        
        for i in range(len(nums)):
            if nums[i] not in hash1:
                continue
            subj1 = nums[i]
            subj2 = nums[i]
            hash1.pop(subj1, None)
            temp_length = 1
            
            while (subj1 + 1) in hash1:
                temp_length += 1
                subj1 = subj1 + 1
                hash1.pop(subj1, None)
            
            while (subj2 - 1) in hash1:
                temp_length += 1
                subj2 = subj2 - 1
                hash1.pop(subj2, None)
            
            if temp_length > longest_len:
                longest_len = temp_length
        
        return longest_len
            

        

            