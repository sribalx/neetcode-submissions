from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # create a hashmap hash_t, so that we know what characters and what count
        # as you go from left to right, add hashmap hash_s, iff hash_s[r] is in hash_t
        # check if hash_s equals hash[t]. if yes, first trim from the left
        # until you find the shortest string. then, move l by and and search again.
        #if no, then move r to the right
        
        if len(s) < len(t):
            return ("")

        result = []
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)
        for char in t:
            hash_t[char] += 1

        for char in t:
            hash_s[char] = 0

        l = 0

        for r in range(len(s)):
            print(s[l:r+1])
            if s[r] in hash_t:
                hash_s[s[r]] += 1
            
            print('rip')
            #print(hash_s, hash_t)
            if all(v >= u for v,u in zip(hash_s.values(),hash_t.values())):
                print('yes')
                flag = 0
                while flag == 0:
                    if s[l] in hash_s:
                        hash_s[s[l]] -= 1
                    if not all(v >= u for v,u in zip(hash_s.values(),hash_t.values())):
                        result.append(s[l:r+1])
                        #hash_s[s[l]] += 1
                        flag = 1
                        print('complete')
                        print(result)
                    l += 1
            
        min_len = 100000000
        corr_ans = [""]
        for thingy in result:
            if len(thingy) < min_len:
                min_len = len(thingy)
                corr_ans[0] = thingy
        
        return corr_ans[0]

            
                    




        '''
        for r in range(0, len(s)):
            if s[r] in hash_t and hash_t[s[r]] > 0:
                print('s[r] in hash_t')
                hash_t[s[r]] -= 1
                print(hash_t)
                print(s[l:r+1])

            if all(v == 0 for v in hash_t.values()):
                print('full string found!')
                print(hash_t)
                result.append(s[l:r + 1])
                hash_t[s[l]] += 1
                l += 1
            else:
                print('move on')
                if s[l] not in hash_t:
                    l += 1
                print(hash_t)
                print(s[l:r+1])
        '''

                    
            