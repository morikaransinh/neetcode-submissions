
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for words in strs:
            sorted_keys = "".join(sorted(words))
            ans[sorted_keys].append(words)
        return list(ans.values())

           
        