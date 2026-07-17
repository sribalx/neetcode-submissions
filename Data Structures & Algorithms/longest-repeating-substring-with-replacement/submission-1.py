from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hash_freq = defaultdict(int)

        # idea is that for a given window of length n,
        # it is valid so long as the frequency of the most frequent character
        # is at least n-k. if it is less, then move the left limit until it is. 
        # then continue moving right limit to the right again.

        max_len = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            hash_freq[s[r]] += 1
            if (r - l + 1) - max(hash_freq.values()) <= k:
                max_len = max(max_len, r - l + 1)
            else:
                hash_freq[s[l]] -= 1
                l += 1
            
        return max_len

        


        