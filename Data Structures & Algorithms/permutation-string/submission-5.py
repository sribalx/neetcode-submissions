from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        s1_hash = [0] * 26
        for char in s1:
            s1_hash[ord(char) - ord('a')] += 1
        
        l = 0
        r = 0
        s2_hash = [0] * 26

        while r < len(s1):
            s2_hash[ord(s2[r]) - ord('a')] += 1
            r += 1
        
        r -= 1
        
        while r < len(s2):
            if s1_hash == s2_hash:
                return True
            else:
                s2_hash[ord(s2[l]) - ord('a')] -= 1
                l += 1
                r += 1
                if r < len(s2):
                    s2_hash[ord(s2[r]) - ord('a')] += 1
        
        return False
