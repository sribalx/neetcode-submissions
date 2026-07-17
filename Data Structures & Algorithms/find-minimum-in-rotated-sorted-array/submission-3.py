import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # there will be two segments of nums, and we binary search in each and compare the smallest
        # find the middle point. point will be where the right term is smaller than the left
        # if nums[i] < nums[i+1], split into nums[0:i+1], nums[i+1:len(nums)]
        if len(nums) == 1:
            return nums[0]

        res_1 = math.inf
        res_2 = math.inf
        break_point = 0
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            #print(break_point, l, r)
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                break_point = mid
                break
            elif nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
            
        if len(nums[0:(break_point+1)]) == 0:
            return min(nums[(break_point+1):])
        if len(nums[(break_point+1):]) == 0:
            return min(nums[0:(break_point+1)])
        else:
            return min(min(nums[0:(break_point+1)]), min(nums[(break_point+1):]))

