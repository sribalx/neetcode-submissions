class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count = [0] * 26
        base = ord('a') 

        for i in range(len(s)):
            count[ord(s[i]) - base] += 1
            count[ord(t[i]) - base] -= 1
        
        for val in count:
            if val != 0:
                return False
         
        return True
        
        
        seen = []
        for char1 in s:
            seen.append(char1)

        for char2 in t:
            if char2 not in seen:
                return False
            seen.remove(char2)

        if seen:
            return False
            
        return True