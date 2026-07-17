class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        max_length = 0
        l = 0
        r = 1
        seen = set()
        count = 1
        seen.add(s[0])

        while r < len(s) and l < len(s):
            
            while s[r] in seen:
                print('nau')
                seen.remove(s[l])
                l += 1
                count -= 1
            
            if s[r] not in seen:
                print('yay')
                seen.add(s[r])
                r += 1
                count += 1

            max_length = max(count, max_length)
            print(seen)


            '''
            seen.add(s[l])
            if s[r + 1] not in seen:
                print('yay')
                r += 1
                seen.add(s[r])
                count += 1
            elif s[r + 1] in seen:
                print('nau')
                l += 1
                r += 1
            max_length = max(max_length, count)
            print(l,r, count, max_length)
            '''
        
        return max_length
