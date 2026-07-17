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
                seen.remove(s[l])
                l += 1
                count -= 1
            
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                count += 1

            max_length = max(count, max_length)

        return max_length
