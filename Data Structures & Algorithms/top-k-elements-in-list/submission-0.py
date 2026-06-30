class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]  = 1
        
        sorted_keys = sorted(hash,key = lambda x:hash[x],reverse = True)
        return sorted_keys[:k]
        