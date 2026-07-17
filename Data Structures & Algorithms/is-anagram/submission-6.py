class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

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