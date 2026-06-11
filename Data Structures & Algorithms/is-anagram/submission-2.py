class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = [0] * 26
        letters2 = [0] * 26
        for ch in s:
            i = ord(ch) - 97
            letters1[i] += 1

        for ch in t:
            i = ord(ch) - 97
            letters2[i] += 1

        if letters1 == letters2:
            return True
        
        return False

