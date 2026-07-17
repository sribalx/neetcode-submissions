from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        diff_hash = defaultdict(int)
        result = []

        for i in range(len(numbers)):
            diff_hash[numbers[i]] = i
        
        for j in range(len(numbers)):
            if (target - numbers[j]) in diff_hash:
                result.append(min((j + 1), (diff_hash[target - numbers[j]] + 1)))
                result.append(max((j+1), (diff_hash[target - numbers[j]]+1)))
                break

        return result
