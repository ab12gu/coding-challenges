class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        repeats = dict()
        start = longest = 0

        for c in range(len(s)):
            if s[c] in repeats and repeats[s[c]] >= start:
                start = repeats[s[c]] + 1
                    
            repeats[s[c]] = c

            if longest < c - start + 1:
                longest = c - start + 1
        
        return longes
