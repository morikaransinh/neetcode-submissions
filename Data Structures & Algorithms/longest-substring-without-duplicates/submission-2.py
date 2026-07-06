class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        hashmap = {}
        maxi = 0
        
        while(i < len(s) and j < len(s)):
            if s[j] not in hashmap:
                hashmap[s[j]] = 1
                
                maxi = max(maxi, j - i + 1)
                j += 1
            else:
                hashmap.pop(s[i], None)
                i += 1
                
        return maxi
