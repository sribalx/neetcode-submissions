from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        diff_hash = defaultdict(int)
        result = []

        for i in range(len(numbers)):
            #difference = target - numbers[i]
            diff_hash[numbers[i]] = i
        
        print(diff_hash)
        
        for j in range(len(numbers)):
            if (target - numbers[j]) in diff_hash:
                print (numbers[j], target - numbers[j])
                print (j, diff_hash[target - numbers[j]])
                result.append(min((j + 1), (diff_hash[target - numbers[j]] + 1)))
                result.append(max((j+1), (diff_hash[target - numbers[j]]+1)))
                break

        return result
