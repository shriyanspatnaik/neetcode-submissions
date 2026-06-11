class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        lst = []
        d = defaultdict(list)
        for word in strs:
            l = [0] * 26
            for letter in word:
                i = ord(letter) - ord('a')
                l[i] += 1
            d[tuple(l)].append(word)       
        for k,v in d.items():
            lst.append(v)
        return lst