from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        
        stak = []
        for i in range(len(s)):

            if s[i] == ']':
                if len(stak) == 0:
                    print('a')
                    return False
                if stak[-1] == '[':
                    stak.pop()
                else:
                    print('b')
                    return False
                
            elif s[i] == '}':
                if len(stak) == 0:
                    print('c')
                    return False
                if stak[-1] == '{':
                    stak.pop()
                else:
                    print('d')
                    return False
            
            elif s[i] == ')':
                if len(stak) == 0:
                    print('e')
                    return False
                if stak[-1] == '(':
                    stak.pop()
                else:
                    print('f')
                    return False
                
            else:
                stak.append(s[i])
            
            print(stak)
        

        if len(stak) == 0:
            return True
        else:
            print('g')
            return False
            
