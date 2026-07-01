class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        for char in s:
            if char.isalnum():
                rev += char.lower()

        if rev == rev[::-1]:
            return True

        return False
