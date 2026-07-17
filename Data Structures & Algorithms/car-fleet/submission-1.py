class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet_count = 0
        stack = []
        time = []
        for i in range(len(speed)):
            time.append((target - position[i])/speed[i])
        
        sorted_cars = []
        for j in range(len(position)):
            sorted_cars.append([j, position[j]])
        sorted_cars.sort(key = lambda x: x[1])

        for k in range (len(position) - 1, -1, -1):
            print('start')
            print(k, stack)
            if len(stack) == 0:
                stack.append(sorted_cars[k])
                continue
            
            print(time[stack[-1][0]], time[sorted_cars[k][0]])
            if time[stack[-1][0]] >= time[sorted_cars[k][0]]:
                continue
            else:
                while len(stack) != 0:
                    stack.pop()
                fleet_count += 1
                print('fleet count updated')
                print(fleet_count)
                stack.append(sorted_cars[k])
        
        if len(stack) != 0:
            fleet_count += 1
            
        return fleet_count
