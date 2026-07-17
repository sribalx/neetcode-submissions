class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:

            if self.isalphanumeric(s[l]) == False:
                l += 1
                continue
            
            if self.isalphanumeric(s[r]) == False:
                r -= 1
                continue
            
            print(s[l].lower(), s[r].lower())
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True


    def isalphanumeric(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')))