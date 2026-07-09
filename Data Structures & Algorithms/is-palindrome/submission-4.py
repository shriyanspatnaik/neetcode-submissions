class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            start = s[i].isalnum()
            end = s[j].isalnum()

            while i < j and not start:
                i += 1
                start = s[i].isalnum()

            while i < j and not end:
                j -= 1
                end = s[j].isalnum()

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

            
        return True