class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            start = s[i].isalnum()
            end = s[j].isalnum()
            if start and end:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            if not start:
                i += 1
            if not end:
                j -= 1
            
        return True