class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        ans = []
        for i in range(len(nums)):
            diff[target - nums[i]] = i
        
        for j in range(len(nums)):
            print (target - nums[j])
            if nums[j] in diff and j != diff[nums[j]]:
                ans.append(j)
                ans.append(diff[nums[j]])
                break

        return ans
        
