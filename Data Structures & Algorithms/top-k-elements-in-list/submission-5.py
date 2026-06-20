class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        ls = list(freq.values())
        ls.sort(reverse = True)
        min = ls[k-1]
        l = [K for K,V in freq.items() if V >= min]
        return l