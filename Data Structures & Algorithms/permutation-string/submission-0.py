class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = {}
        hashmap_s2 = {}
        for ch in s1:
            if ch in hashmap_s1:
                hashmap_s1[ch] += 1
            else:
                hashmap_s1[ch] = 1

        i = 0
        j = 0

        while j < len(s2):
            if s2[j] in hashmap_s2:
                hashmap_s2[s2[j]] += 1
            else:
                hashmap_s2[s2[j]] = 1
            if j - i + 1 == len(s1):

                if hashmap_s1 == hashmap_s2:
                    return True

                
                hashmap_s2[s2[i]] -= 1
                if hashmap_s2[s2[i]] == 0:
                    del hashmap_s2[s2[i]]

                i += 1

            j += 1

        return False