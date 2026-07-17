from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)
        freq = defaultdict(list)

        for num in nums:
            count[num] += 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        #print(freq)

        res = []
        for i in range(len(nums), 0, -1):
            print(i)
            #print(freq)
            for num in freq[i]:
                #print('hooray')
                res.append(num)
                print(res)
                if len(res) == k:
                    return res
        

        
        '''
        for i in range(k):
            largest_value = 0
            largest_key = 0
            for key, value in hashmap.items():
                if value > largest_value:
                    largest_value = value
                    largest_key = key
            
            result.append(largest_key)
            del hashmap[largest_key]
        

        freq = defaultdict(list)
        for j in range(20):
            freq[hashmap[j]].append(j)
        
        print(freq)

        for a in range (len(nums), 0, -1):
            result = result + freq[a]
            if len(result) == k:
                return result
        '''
