from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # create a hashmap hash_t, so that we know what characters and what count
        # as you go from left to right, add hashmap hash_s, iff hash_s[r] is in hash_t
        # check if hash_s greater than or equal to hash[t]. if yes, first trim from the left
        # until hash_s is not greater than or equal to hash[t]. then, move l by and and search again.
        #if no, then move r to the right
        
        # easy cut at start
        if len(s) < len(t):
            return ("")

        # populate both hashmaps. hash_s only tracks the letters also in hash_t
        result = []
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)
        for char in t:
            hash_t[char] += 1
            hash_s[char] = 0

        l = 0

        for r in range(len(s)):
            if s[r] in hash_t:
                hash_s[s[r]] += 1 # add to hash_s if the thing exists
            
            if all(v >= u for v,u in zip(hash_s.values(),hash_t.values())): # checking if all values in s are greater than or equal
                flag = 0
                while flag == 0:
                    if s[l] in hash_s: 
                        hash_s[s[l]] -= 1
                    if not all(v >= u for v,u in zip(hash_s.values(),hash_t.values())): # slashing until hash_s values are less than hash_t
                        result.append(s[l:r+1])
                        flag = 1
                    l += 1 # move left by one and then exit this loop, keep searching

        # find shortest substring
        if result:
            shortest_string = min(result, key = len)
            return shortest_string
        else:
            return("")

                    
            