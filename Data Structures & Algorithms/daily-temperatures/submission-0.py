class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            print(stack)
            if len(stack) == 0:
                stack.append([temperatures[i], i])
                continue
            print (temperatures[i], stack[-1][0])
            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])
        
        return result

            
