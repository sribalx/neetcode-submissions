class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                print(s[j], j)
                j += 1
                #print(j)
                if j >= len(s):
                    return result
            length = int(s[i:j])
            print(length)
            print('damn')
            i = j + 1
            j = j + length + 1
            result.append(s[i:j])
            i = j
            #print(result)
        
        return result
