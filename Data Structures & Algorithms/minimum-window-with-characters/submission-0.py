class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap_t = {}
        hashmap_s = {}

        for ch in t:
            if ch in hashmap_t:
                hashmap_t[ch] += 1
            else:
                hashmap_t[ch] = 1

        required = len(hashmap_t)
        formed = 0

        i = 0
        j = 0

        mini = float("inf")
        start = 0

        while j < len(s):

            if s[j] in hashmap_s:
                hashmap_s[s[j]] += 1
            else:
                hashmap_s[s[j]] = 1

            if s[j] in hashmap_t and hashmap_s[s[j]] == hashmap_t[s[j]]:
                formed += 1

            while formed == required:

                if j - i + 1 < mini:
                    mini = j - i + 1
                    start = i

                hashmap_s[s[i]] -= 1

                if s[i] in hashmap_t and hashmap_s[s[i]] < hashmap_t[s[i]]:
                    formed -= 1

                i += 1

            j += 1

        if mini == float("inf"):
            return ""

        return s[start:start + mini]