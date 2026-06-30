class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(word + ":haha:" for word in strs)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = s.split(":haha:")
        return res[:-1]
