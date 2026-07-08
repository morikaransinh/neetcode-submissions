class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        i = 0
        maxi = 0
        max_freq = 0

        for j in range(len(s)):
            hashmap[s[j]] = hashmap.get(s[j], 0) + 1

            max_freq = max(max_freq, hashmap[s[j]])

            while (j - i + 1) - max_freq > k:
                hashmap[s[i]] -= 1
                i += 1

            maxi = max(maxi, j - i + 1)

        return maxi